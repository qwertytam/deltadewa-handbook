---
title: "Crash Payoff Ratio / Tail Hedge Effectiveness"
---

See [Ratio Disambiguation](ratio-disambiguation.md) for how this metric differs
from Crash Convexity, which shares its numerator but not its denominator.

## Definition of Crash Payoff Ratio

Crash payoff ratio measures how much of the portfolio loss is offset by the hedge during a crash. This metric evaluates hedge effectiveness, not convexity [[Bhansali 2014]](../footnotes/index.md#bhansali), [[Meketa 2019]](../footnotes/index.md#meketa), [[Cambridge Associates 2025]](../footnotes/index.md#cambridge), [[CAIA 2021]](../footnotes/index.md#caia).

It answers:
> If markets crash, how much of the loss does the hedge absorb?

## Crash Payoff Ratio Metric

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
Hedge profit   = +$1.5M
```

Result:

```text
Crash Payoff Ratio = 1.5M / 2.5M = 60%
```

*Interpretation:* 60% of the equity drawdown is offset by the hedge at a −25% SPX decline

## Interpretation of Crash Payoff Ratio

Typical ranges:

| Ratio     | Meaning                   |
| --------- | ------------------------- |
| < 20%     | hedge largely ineffective |
| 20 to 40% | partial protection        |
| 40 to 80% | strong tail hedge         |
| > 80%     | very aggressive hedge     |

Most long-equity hedge programs aim for the **strong tail hedge** band above — a
40 to 80% loss offset at a −25% market decline. That offset provides the
liquidity to rebalance portfolios during a crisis.

Read against [Crash Convexity](crash-convexity.md), that band is the same
statement in the other denominator: at −25% SPX the equity loss is a quarter of
portfolio value, so a 40 to 80% offset is a 10 to 20% crash convexity. Both are
owned by
[Typical Hedge Program Targets](../part-7/typical-hedge-program-targets.md#typical-institutional-targets).

## Important Caveat

The ratio is only meaningful when stated alongside its explicit scenario assumptions — the assumed market decline, the vol spike applied, and whether skew steepening is modelled. A ratio stated without these inputs cannot be compared across programs or structures.
