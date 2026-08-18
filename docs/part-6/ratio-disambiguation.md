---
title: "Ratio Disambiguation"
---

Seven ratios recur throughout this handbook, and several of them have been given
more than one name in common practice. Two of those names differ only in word
order while meaning the same thing; one pair looks interchangeable and is not.
This page is the reference for which is which.

Read it as a disambiguation aid rather than as a substitute for the metric
pages. Each row links to the page that develops the metric properly, and those
pages hold the worked examples and the full interpretation tables.

## The Seven Ratios

| Metric | Also called | Numerator over denominator | Headline band |
| ------ | ----------- | -------------------------- | ------------- |
| [Crash Convexity](crash-convexity.md) | Crisis payout; crisis hedge gain as % of portfolio | Hedge gain in the crash, over **portfolio value** | See [Crash Convexity](crash-convexity.md#interpretation-of-crash-convexity) |
| [Crash Payoff Ratio](crash-payoff-ratio-tail-hedge-effectiveness.md) | Offset ratio; loss offset; tail hedge effectiveness | Hedge gain in the crash, over **portfolio equity loss in that same crash** | 25 to 40% offset at −25% |
| [Crash Payoff per Unit of Notional](#crash-payoff-per-unit-of-notional) | Per-notional payoff rate; payoff per dollar of notional | Hedge gain in the crash, over **hedge notional** | No general band |
| [Payoff-vs-Premium Multiple](#payoff-vs-premium-multiple) | No settled synonym | Hedge value in the crash, over **hedge value today** | No general band |
| [Hedge Efficiency Ratio](hedge-efficiency-ratio.md) | Carry-Convexity Ratio; convexity/carry ratio. **"Carry-to-Convexity" is a different quantity** — see below | Crash convexity (% of portfolio), over **annual carry (% of portfolio)** | Under 3 poor; 3 to 6 acceptable; above 6 attractive |
| [Theta Carry](theta-carry-insurance-cost.md) | Annual carry; insurance cost. **"Annual carry budget" in a backtest is a different quantity** — see below | Annualised hedge time decay, over **portfolio value** | See [Annual Premium Budget Bands](../part-7/typical-hedge-program-targets.md#annual-premium-budget-bands) |
| [Vega Sufficiency](vega-sufficiency.md) | Vega exposure; vega term exposure | Portfolio vega, over **portfolio value** | See [Typical Hedge Program Targets](../part-7/typical-hedge-program-targets.md) |

The denominators are what separate these ratios. Four different quantities sit
under the line — portfolio value, portfolio equity loss, hedge value and hedge
notional — and two ratios that share a numerator can still answer entirely
different questions.

## Notes on Individual Metrics

### Crash Convexity

The scenario hedge gain as a fraction of the portfolio being protected. Because
its denominator is portfolio value, it combines cleanly with any other ratio
carrying the same denominator — which is what makes it, not the crash payoff
ratio, the right numerator for hedge efficiency.

The headline band is deliberately left to the owning page here. Two pages in the
handbook currently state different target ranges for it, and picking one in a
summary table would settle that by formatting rather than by decision.

### Crash Payoff Ratio

Answers how much of the *loss* the hedge absorbs, so its denominator is the
portfolio's equity loss in the crash rather than the portfolio's value. This is
the only one of the seven whose denominator moves with the severity of the
scenario, which is why the ratio is meaningless when quoted without its scenario
assumptions.

"Offset ratio" is the same quantity and appears under that name in PART VII.

Because it is silent about hedge size, it cannot be used to size a hedge. That
is the job of the next ratio, and the two are easily confused: both divide a
crash gain, but one divides it by what the portfolio lost and the other by what
the hedge cost to put on in notional terms.

### Crash Payoff per Unit of Notional

The only one of the seven whose denominator is the hedge rather than the
portfolio: what one dollar of hedge notional returns in the crash scenario.

$$\text{Crash Payoff per Unit of Notional} = \frac{\text{Hedge Gain in the Crash}}{\text{Hedge Notional}}$$

This is the quantity that converts a required payoff into a hedge size, which is
why it is the divisor in
[Portfolio Hedge Sizing Framework](../part-7/portfolio-hedge-sizing-framework.md#sizing-to-the-risk-budget).
A crash payoff ratio cannot do that job — its denominator is the portfolio's
equity loss, so it says how much of the loss the hedge absorbs while saying
nothing about how large the hedge is.

Like every crash-scenario figure it is meaningless without its scenario: the
same book's per-notional payoff rate is higher at −35% than at −25%.

No general band is given. The rate is a function of strike distance, remaining
tenor and crash depth rather than a program target — deeper strikes lower it,
deeper crashes raise it — so it enters the sizing calculation as a modelled
input, taken from the repricing exercise in
[A4 Crash Repricing Methodology](../appendices/a4-crash-repricing-methodology.md).

### Payoff-vs-Premium Multiple

The crudest of the seven, and the only one usually quoted as a multiple rather
than a percentage: what the hedge is worth in the crash, divided by what it is
worth now.

$$\text{Payoff-vs-Premium Multiple} = \frac{V_{crash}}{V_{today}}$$

At inception the denominator is the premium paid, which is where the name comes
from. For a seasoned position it is the current mark, and the distinction
matters — dividing a crash valuation by a premium paid two years ago mixes a
historical cost with a present value and produces a number that flatters or
punishes the hedge purely according to what has happened since.

It is a **gross** ratio: unlike crash convexity it does not net off the hedge's
current value, so a multiple of 17.5× and a convexity figure are not two views of
the same arithmetic. The worked example in
[A4 Crash Repricing Methodology](../appendices/a4-crash-repricing-methodology.md#worked-example)
reports both, and also shows why the basis matters — the same book reads 17.5× on
repriced values and 2.5× on intrinsic values.

No general band is given because none exists that is not a program's own choice.
The multiple is a function of crash depth, strike distance and remaining tenor,
and a book can raise it arbitrarily by holding cheaper, deeper strikes.

### Hedge Efficiency Ratio

Crash convexity divided by annual carry: how much crash payoff a program buys
per unit of annual cost. Both numerator and denominator are percentages of
portfolio value, so the ratio reads directly as payoff per dollar of carry.

Three names refer to this same quantity: **Hedge Efficiency Ratio**,
**Carry-Convexity Ratio**, and **convexity/carry ratio**. The first is primary.

!!! warning

    A fourth name, **"Carry-to-Convexity"**, appears in PART VII with a
    *different* formula — crash payoff **ratio** over annual carry budget. Its
    numerator is divided by portfolio equity loss rather than portfolio value, so
    it is not this metric under another name and its value will not match. Two
    ratios built from different denominators cannot be compared, and a figure
    quoted under that name should be recomputed before it is read against the
    bands above.

### Theta Carry

The annualised cost of holding the hedge, as a fraction of the portfolio.

!!! note

    "Annual carry budget" as used in backtesting is **premiums paid less
    monetization gains**, over portfolio value. That is a realised, net figure
    covering a historical period; theta carry is a forward-looking accrual read
    off the current position. They answer different questions and will not agree.

### Vega Sufficiency

Portfolio vega over portfolio value. PART X refers to the same normalisation as
"vega term exposure"; several desks use alternative denominators — vega per 1%
underlying move, or vega per unit of variance shock — which are noted on the
owning page and are not interchangeable with the primary form.
