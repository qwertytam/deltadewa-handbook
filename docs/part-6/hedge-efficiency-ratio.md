---
title: "Hedge Efficiency Ratio"
---

Measures how much downside risk the hedge offsets relative to cost. It is a summary statistic rather than a standalone risk metric.

It is also called the **Carry-Convexity Ratio**, particularly in a dashboard context. The two names describe the same quantity — crash payoff divided by annual carry — and this page is the single definition for both.

It does not introduce new information beyond:

- Crash Payoff Ratio
- Theta Carry

## HER Metric

$\text{Hedge Efficiency} = \frac{\text{Crash payoff}}{\text{Annual carry}}$

or using percentage terms

$\text{Hedge Efficiency} = \frac{\text{Crash payoff \%}}{\text{Annual carry \%}}$

<a id="hedge-efficiency-dollar-worked-example"></a>

*Example:*

For:

```text
Crash payoff = $1.5M
Annual Carry = $300k
```

Result:

```text
Efficiency = 1.5M / 300k = 5x payoff relative to cost
```

## Mathematical Definition of the Ratio

The same ratio, written in the convexity-and-carry terms used by the PART X dashboard:

$\text{Carry-Convexity Ratio} = \frac{\text{Convexity}}{\text{Carry}}$

Crash convexity is the crash payoff expressed as a percentage of portfolio value, so this is the percentage form of the formula above under its other name.

<a id="convexity-carry-worked-example"></a>

If crash convexity at −25% SPX is 22% and annual carry is 3%, then the ratio is:

```text
22% / 3% = 7.3
```

## Interpretation of the Ratio

| Ratio  | Meaning    |
| ------ | ---------- |
| < 3    | poor hedge |
| 3 to 6 | acceptable |
| > 6    | attractive |

Tail funds prefer **high convexity relative to cost**.

Typical values for the two inputs are owned elsewhere: see [Typical Institutional Targets](../part-7/typical-hedge-program-targets.md#typical-institutional-targets) for annual carry, and [Crash Convexity](crash-convexity.md) for the crash-convexity band.

See [Carry vs. Convexity Chart](../part-10/tier-1-core-hedge-metrics.md#5-carry-vs-convexity-chart) in PART X for how the trade-off is displayed on a dashboard.
