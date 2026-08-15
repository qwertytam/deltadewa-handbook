---
title: "Crash Payoff Ratio / Tail Hedge Effectiveness"
---

#### Definition of Crash Payoff Ratio

Crash payoff ratio measures how much of the portfolio loss is offset by the hedge during a crash. This metric evaluates hedge effectiveness, not convexity [[Bhansali 2014]](../footnotes/index.md#bhansali)[[Meketa 2019]](../footnotes/index.md#meketa)[[Cambridge Associates 2025]](../footnotes/index.md#cambridge)[[CAIA 2021]](../footnotes/index.md#caia).

It answers:
> If markets crash, how much of the loss does the hedge absorb?

#### Crash Payoff Ratio Metric

Let:

$Portfolio \ Loss$ = portfolio decline under crash scenario

$Hedge\ Gain$ = hedge profit under same scenario

Define:

$\text{Crash Payoff Ratio} = \frac{Hedge\ Gain}{Portfolio\ Equity\ Loss} \times 100\%$

Example:

```text
Portfolio      = $10M
Scenario       = SPX −25%
Portfolio loss = −$2.5M
Hedge profit   = +$800k
```

Result:

```text
Crash Payoff Ratio = 800k / 2.5M = 32%
```

*Interpretation:* 32% of the equity drawdown is offset by the hedge at a −25% SPX decline

#### Interpretation of Crash Payoff Ratio

Typical ranges:

| Ratio     | Meaning                   |
| --------- | ------------------------- |
| < 10%     | hedge largely ineffective |
| 10 to 25% | partial protection        |
| 25 to 40% | strong tail hedge         |
| > 40%     | very aggressive hedge     |

Most long-equity hedge programs aim for:

```text
20 to 35% loss offset at −25% market decline
```

This provides liquidity to rebalance portfolios during crises.

#### Important Caveat

The ratio is only meaningful when stated alongside its explicit scenario assumptions — the assumed market decline, the vol spike applied, and whether skew steepening is modelled. A ratio stated without these inputs cannot be compared across programs or structures.

