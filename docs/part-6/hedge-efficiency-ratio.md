---
title: "Hedge Efficiency Ratio"
---

Measures how much downside risk the hedge offsets relative to cost. It is a summary statistic rather than a standalone risk metric.

It is also called the **Carry-Convexity Ratio**, particularly in a dashboard context. The two names describe the same quantity — the hedge's crash gain divided by its annual carry — and this page is the single definition for both. See [Ratio Disambiguation](ratio-disambiguation.md) for how this ratio differs from the similarly named ones.

It does not introduce new information beyond:

- Crash Convexity
- Theta Carry

## HER Metric { #her-metric }

In dollar terms, the numerator is the hedge's gain in the crash and the denominator its annual cost to hold:

$\text{Hedge Efficiency} = \frac{\text{Crash payoff \$}}{\text{Annual carry \$}}$

Dividing both by portfolio value leaves the ratio unchanged and gives the percentage form, in which the numerator is crash convexity:

$\text{Hedge Efficiency} = \frac{\text{Crash convexity \%}}{\text{Annual carry \%}}$

!!! warning

    The numerator is crash convexity — hedge gain over **portfolio value** — and
    not the Crash Payoff Ratio, whose denominator is the portfolio's **equity
    loss**. The two are easily confused because both are percentages describing
    the same crash. Substituting one for the other changes the result and
    invalidates the bands below.

*Example:*
{ #hedge-efficiency-dollar-worked-example }

For:

```text
Crash payoff = $1.5M
Annual Carry = $300k
```

Result:

```text
Efficiency = 1.5M / 300k = 5x payoff relative to cost
```

## Mathematical Definition of the Ratio { #mathematical-definition-of-the-ratio }

The same ratio, written in the convexity-and-carry terms used by the PART X dashboard:

$\text{Carry-Convexity Ratio} = \frac{\text{Convexity}}{\text{Carry}}$

Crash convexity is the crash payoff expressed as a percentage of portfolio value, so this is the percentage form of the formula above under its other name.

If crash convexity at −25% SPX is 22% and annual carry is 3%, then the ratio is:
{ #convexity-carry-worked-example }

```text
22% / 3% = 7.3
```

The inputs here are chosen to demonstrate the arithmetic, not to describe a
book at target: 22% crash convexity sits above the program band in
[Typical Hedge Program Targets](../part-7/typical-hedge-program-targets.md#typical-institutional-targets),
and the ratio would be read against the interpretation table below regardless.
A convexity figure has to carry its crash scenario before it can be compared to
that band at all.

## Interpretation of the Ratio { #interpretation-of-the-ratio }

| Ratio  | Meaning    |
| ------ | ---------- |
| < 3    | poor hedge |
| 3 to 6 | acceptable |
| > 6    | attractive |

Tail funds prefer **high convexity relative to cost**.

Typical values for the two inputs are owned elsewhere: see [Annual Premium Budget Bands](../part-7/typical-hedge-program-targets.md#annual-premium-budget-bands) for annual carry, and [Crash Convexity](crash-convexity.md) for the crash-convexity band.

See [Carry vs. Convexity Chart](../part-10/tier-1-core-hedge-metrics.md#5-carry-vs-convexity-chart) in PART X for how the trade-off is displayed on a dashboard.
