---
title: "Crash Convexity"
---

See [Convexity](../part-5/convexity.md) for additional detail on convexity.

Crash convexity incorporates three drivers discussed earlier:

- See [Delta acceleration (gamma)](../part-2/gamma.md)
- See [Volatility expansion (vega)](../part-2/vega.md)
- See [Skew steepening](../part-3/volatility-skew.md)

## Crash Convexity Metric

Crash convexity is typically evaluated using scenario analysis.

!!! note

    There is no single universally standardised formula — see
    [Why There Is No Single Standard](#why-there-is-no-single-standard) for
    further detail.

Let:

$V_{today}$ = current hedge value

$V_{crash}$ = hedge value after a simulated crash

$Portfolio$ = portfolio value

Define:

$\text{Crash Convexity}_x = \frac{V_{crash} − V_{today}}{Portfolio}$

> This definition leaves $V_{crash}$'s repricing mechanics unspecified.
> See [A4 Crash Repricing Methodology](../appendices/a4-crash-repricing-methodology.md) for how the
> implementation forms it — hedge-only, repriced rather than intrinsic,
> instantaneous, on a skew-aware volatility shock — and
> [`docs/repricing-methodology.md`](https://github.com/qwertytam/deltadewa/blob/main/docs/repricing-methodology.md) for the normative
> specification and its acceptance tests.

Where:

$x$ is the assumed market decline (e.g. 20%, 30%, 40%)

This is a scenario P&L ratio — it measures how much the hedge gains as a percentage of the portfolio under a given crash assumption. Other names include:

```text
Crisis Payout
or
Crisis Hedge Gain (% of portfolio)
```

It is simple, intuitive, and the most widely used formulation among institutional desks and family offices.

Example:

```text
Portfolio = $10M
Hedge value today = $150k
Hedge value if SPX −25% = $1.2M
```

```text
Crash Convexity = (1.2M − 150k) / 10M = 10.5%
```

## Interpretation of Crash Convexity

Typical institutional ranges:

| Crash Convexity | Interpretation             |
| --------------- | -------------------------- |
| < 5%            | weak crash protection      |
| 5 to 15%        | moderate hedge             |
| 15 to 30%       | strong tail hedge          |
| > 30%           | very aggressive protection |

Most institutional programs target:

```text
10 to 25% crash convexity at −20% to −30% SPX
```

Higher convexity usually requires:

```text
more vega exposure
deeper OTM strikes
higher carry cost
```

## Why There Is No Single Standard

Unlike delta or vega, crash convexity is not a derivative of the pricing function. It is a scenario output, not a closed-form greek. The result depends on three modelling choices:

### 1. The crash scenario itself

Most programs run multiple: typically −15%, −20%, −25%, −30%, and sometimes −40% to capture both moderate corrections and severe crashes. Reporting a single number without specifying the scenario is incomplete.

### 2. How to reprice the hedge

This is where firms differ most. Options include:

#### Full Surface Reprice

Shift spot down by x% and simultaneously apply a historically-calibrated vol surface shift (including skew steepening). This is the most realistic and preferred by sophisticated programs.

#### Delta-only approximation

$\Delta V \approx \Delta_{hedge} \times \Delta S$

Fast but significantly understates convexity because it ignores vega and skew.

#### Delta + vega approximation

$\Delta V \approx \Delta_{hedge} \times \Delta S + \nu \times \Delta\sigma$

Better, but still assumes parallel vol shifts rather than skew steepening.

### 3. Whether to Include or Exclude the Initial Premium Paid

Some firms report gross hedge P&L; others report net of carry cost paid to date. These produce materially different numbers.

## A Slightly More Complete Version

For programs that want to make the vol assumption explicit:

$\text{Crash Convexity}_x = \frac{\Delta_{hedge} \cdot \Delta S + \nu \cdot \Delta\sigma(x) + \text{Skew Adjustment}(x)}{P}$

Where $\Delta\sigma(x)$ is the assumed vol spike at crash level $x$, and the skew adjustment captures non-parallel surface repricing for deep OTM strikes. In practice, few firms compute this analytically — they use a scenario engine to reprice the full position instead.

## What Family Offices and Institutional Investors Actually Use

### Family Offices and Smaller Programs

Family offices and smaller programs typically use the simple scenario ratio with one or two spot shocks (often −20% and −30%), repriced using either a flat vol bump or a vol lookup table calibrated to historical regimes. The goal is a number they can monitor monthly and compare against their carry cost.

### Institutional Tail Funds (Universa, Ambrus, LongTail Alpha etc.)

Institutional tail funds run full surface shock scenarios with explicit skew steepening assumptions, typically computing crash convexity across a grid of spot × vol scenarios. They will often report a convexity profile — a curve rather than a single number — to show how the hedge responds across different crash severities.

### Important Practical Point

The most important practical point is that crash convexity is only meaningful when specified with its scenario assumptions. A number quoted as "28% crash convexity" is incomplete without knowing whether that is at −20% or −30% SPX, and whether it assumes a historical vol spike or a flat parallel shift.

## Example Convexity Profile / Multi-Scenario Table

| Scenario (SPX move) | Vol assumption | Hedge gain | Crash Convexity |
| ------------------- | -------------- | ---------- | --------------- |
| −15%                | +8 vol pts     | \$180k     | 1.8%            |
| −20%                | +15 vol pts    | \$500k     | 5.0%            |
| −25%                | +25 vol pts    | \$1.05M    | 10.5%           |
| −30%                | +35 vol pts    | \$2.1M     | 21.0%           |
| −40%                | +50 vol pts    | \$4.8M     | 48.0%           |
