---
title: "Vega Sufficiency"
---

Vega sufficiency measures whether the hedge has **enough volatility exposure** to benefit from the **volatility spike that usually accompanies a market crash**. Vega sufficiency is typically **scenario based**, not a static ratio.

In equity markets:

```text
market down → volatility up
```

So good hedges should benefit from both:

1. price drop
2. volatility spike

## Portfolio Metric Definition

Let:

$\nu = \frac{\partial V}{\partial \sigma}$ be vega

Define:

$\text{Vega Sufficiency} = \frac{\text{Portfolio Vega}}{\text{Portfolio Value}}$

Some managers scale it relative to expected vol spike:

$\text{Expected Vega Gain} = \nu \times \Delta \sigma$

Institutional programs usually normalize vega to portfolio **notional**, not underlying value. Alternatives to above definition of vega sufficiency include:

```text
vega / 1% underlying move
vega / expected variance shock
```

## Common Metrics for Vega Sufficiency

Primary metric:

```text
portfolio vega / portfolio value
```

Alternative normalizations used by some desks:

```text
vega / delta
vega / variance exposure
```

!!! note

    Variance exposure is also known as expected variance shock.

*Example:*

Portfolio:

```text
$10M equities
```

Hedge:

```text
vega = $15,000 per 1 vol point
```

If volatility rises:

```text
20% → 40%
```

Change:

```text
Δσ = 20 vol points
```

Profit:

```text
Expected vega gain = vega x Δvol
$15,000 × 20 = $300,000
```

For example, in March 2020, the VIX rose from a starting level of approximately 12 to 14, reaching a peak of approximately 82 to 85 at the height of the crisis.

## Portfolio Interpretation of Vega Sufficiency

If vega is too small:

```text
price drop helps
vol spike doesn't
```

Effective crash hedges typically rely heavily on vega exposure.

Long-dated options typically provide stronger vega.
