---
title: "Volatility Skew"
---

## Definition of Volatility Skew

In equity options markets, implied volatility varies across strikes.
This variation is called **volatility skew**.

Instead of all strikes having the same volatility (as assumed in Black-Scholes), the market typically prices **lower strikes with higher implied volatility** than higher strikes.

This produces the characteristic **downward-sloping skew curve**.

Example structure:

```text
OTM puts > ATM > OTM calls
```

This reflects demand for crash protection.

Graphically:

```text
vol
 ^
 |\
 | \
 |  \
 |
 +------ strike
```

Where:

- lower strikes correspond to **downside protection**
- higher strikes correspond to **upside optionality**

*Example:* “Equity puts have downside skew.”

## Why Skew Exists

In equity markets, investors have strong demand for **downside protection**, particularly from:

- asset managers
- pension funds
- structured-product hedging
- portfolio insurance strategies

This persistent demand pushes up the price of OTM puts relative to other options, resulting in higher implied volatility for lower strikes.

As a result:

```text
OTM puts therefore trade at structurally higher implied volatility than ATM options.
```

## Practical Skew Metrics

Traders rarely measure skew using raw strike derivatives.
Instead they use **delta-based metrics**, which are more stable across maturities.

A common definition is:

$Skew = \sigma_{25\Delta\ put} - \sigma_{ATM}$

Where:

- $25\Delta_{put} \approx 10\ to\ 15\% \text{ OTM}$

In practice traders often approximate ATM volatility using the 50$\Delta$ call
or the 40 to 50$\Delta$ put depending on convention.

Example:

| Strike         | IV  |
| -------------- | --- |
| ATM            | 20% |
| 25$\Delta$ put | 27% |

Result:

```text
Skew = 27 − 20 = 7 vol points
```

## Interpretation of Volatility Skew

Skew represents the *market price of crash protection* aka *crash insurance*

When skew is:

Low
→ downside protection relatively cheap.

High
→ investors already paying large premiums for crash insurance.

Because skew varies through time, tail-hedge programs often track **skew percentiles** relative to historical ranges when deciding when to add or reduce protection.

## Skew Percentile

Because skew varies over time, institutional desks often evaluate skew relative to history.

$\text{Skew Percentile}=\text{rank of current skew vs historical distribution}$

This page owns the skew percentile bands. Three of them drive action —
accumulate below the 30th percentile, stay neutral from 30 to 70, avoid buying
above 70 — and they live here, with the measure, rather than on
[Typical Hedge Program Targets](../part-7/typical-hedge-program-targets.md).
The distinction is that every band on that page is something a program chooses,
while this one is a reading of the market and is the same for every program
regardless of its targets. Parts VII and X apply these bands and link back.

| Percentile | Interpretation                    | Action     |
| ---------- | --------------------------------- | ---------- |
| < 30%      | protection historically cheap     | accumulate |
| 30 to 70%  | normal                            | neutral    |
| 70 to 80%  | moderately expensive              | avoid      |
| 80 to 90%  | protection historically expensive | avoid      |
| > 90%      | panic pricing                     | avoid      |

The five descriptive rungs are gradations inside the three action bands, not a
competing scheme. The top three all read as *avoid*; they differ in how far past
the threshold the market has gone, which is why the vocabulary is worth keeping.
Above the 90th percentile the reading carries a further implication — protection
that expensive is usually a signal to monetize existing hedges rather than to
hold and wait, covered in
[Tail Hedge Decision Matrix](../part-10/tail-hedge-decision-matrix.md).

Typical hedge dashboards display:

```text
Skew percentile (trailing 5 years): 22%
Interpretation: protection cheap
```

### The Lookback Window

A percentile is meaningless without the window it is ranked against, and **no
exchange, regulator or standard-setting body publishes one**. A trailing one
year is the common default in vendor and retail analytics, but it is a market
habit rather than a convention anyone has defined, and it is not specific to
skew.

This handbook uses a **trailing five years** throughout, by editorial
convention and with no citation implied. Five years is long enough to contain
at least one genuine stress episode — without which the upper half of the
distribution is unpopulated and every reading looks expensive — while still
short enough that the measure responds to the prevailing volatility regime
rather than to conditions a decade gone.

The choice is a trade-off, not a right answer, and a program is free to make a
different one provided it states the window every time it quotes a percentile.
Longer windows are available: Cboe publishes daily SKEW index history back to
2 January 1990 [[Cboe SKEW Historical Data]](../footnotes/index.md#cboe-skew-historical),
which supports full-history ranking for research purposes where a
regime-responsive reading is not what is wanted.

### Two Different Measures Called "Skew"

Two quite different quantities are ranked into a percentile and both get called
skew. They are not interchangeable, and a percentile computed from one should
never be read against a band calibrated on the other.

| | 25$\Delta$-based skew measure | Cboe SKEW index |
| --- | --- | --- |
| What it is | A volatility *spread*: 25$\Delta$ put IV minus 25$\Delta$ call IV (the 25$\Delta$ risk reversal), or 25$\Delta$ put IV minus ATM IV | A single published index level derived from the risk-neutral skewness of the 30-day SPX log-return distribution |
| How it is built | Two points read off the volatility surface | The whole strip of out-of-the-money SPX options, by the same replication maths as VIX |
| Who defines it | No one — computed in-house, with the tenor, the interpolation and even the delta convention varying between desks | Cboe, by published methodology |
| Units | Volatility points | Index points, where 100 is a normal (zero-skew) distribution and higher means more negative tail skew |
| Comparability | Not comparable between desks without knowing each one's conventions | Directly comparable, being one published series |

Most institutional dashboards measure skew using a 25$\Delta$ risk reversal or
the 25$\Delta$-put-minus-ATM difference, because those read directly off the
surface a program actually trades against. The trade-off is that there is no
standard behind them: two desks quoting "the 25-delta skew" for the same day
can legitimately disagree, so a figure travels only with its conventions
attached. The SKEW index has the opposite profile — one fixed methodology and
one published series, at the cost of describing the whole 30-day distribution
rather than the specific strikes a ladder occupies
[[Cboe SKEW Methodology]](../footnotes/index.md#cboe-skew-methodology).

!!! warning "The distinction may not survive"

    The contrast above is drawn against SKEW as Cboe **currently** calculates
    it. In May 2025 Cboe opened a public consultation proposing to replace the
    moment-based methodology with a differential or ratio of 25-delta put and
    call strikes; in July 2025 its Index Committee determined that
    modifications are appropriate, without publishing a new formula or an
    effective date. Should that change be adopted, SKEW would become a
    25$\Delta$-based measure and the architectural difference described here
    would narrow to a difference of convention only. Check Cboe's current
    methodology before relying on the distinction
    [[Cboe SKEW Methodology]](../footnotes/index.md#cboe-skew-methodology).
