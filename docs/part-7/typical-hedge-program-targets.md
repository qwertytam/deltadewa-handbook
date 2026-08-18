---
title: "Typical Hedge Program Targets"
---

Typical institutional allocations range between 1 to 3% annual carry. Very large macro funds may allocate 3 to 5%.

## Typical Institutional Targets

| Target             | Typical range                   |
| ------------------ | ------------------------------- |
| Carry budget       | 1 to 3% per year                |
| Crash convexity    | 10 to 25% @ −25% SPX            |
| Crash payoff ratio | 25 to 40%                       |
| Vega exposure      | \$1k to \$3k per \$1M portfolio |
| Skew exposure      | positive                        |
| Roll interval      | 9 to 12 months remaining        |

Crash convexity — the hedge's crash gain as a share of portfolio value — is
banded here, and the scenario is part of the band: **10 to 25% at −25% SPX**.
A convexity figure quoted at any other crash depth is a different number and
cannot be read against this range, because a hedge's gain is convex in the size
of the move while the portfolio's value is not. The metric itself is defined,
worked through and interpreted in
[Crash Convexity](../part-6/crash-convexity.md).

The crash payoff ratio — the share of the portfolio's equity loss the hedge
offsets, and the quantity PART VII elsewhere calls the *offset ratio* — is
defined, worked through and banded in
[Crash Payoff Ratio / Tail Hedge Effectiveness](../part-6/crash-payoff-ratio-tail-hedge-effectiveness.md#interpretation-of-crash-payoff-ratio).
The band in the table above is that page's, and like every crash-scenario
figure it is meaningful only against the scenario it is quoted for.

## Typical Tail Hedge Structure

Strike ladder:

```text
35% allocation → 20% OTM strike puts
40% allocation → 30% OTM strike puts
25% allocation → 40% OTM strike puts
```

Tenor ladder:

```text
1/3 position opened every quarter
maintain 12 to 24 month maturity
```

## Annual Premium Budget Bands

This section is the handbook's reference point for what a hedge program costs per year. Other pages link here rather than restating a range of their own.

Several bands are in common use. They differ because of **who is running the program** and **how the hedge is structured** — not because one of them is the correct answer and the others are approximations of it.

| Program Type                             | Typical Annual Premium | What distinguishes it                                                                                                                            |
| ---------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Family office (cost-sensitive)           | 0.5–1.5% of AUM        | Carry is a visible line item that must be defended annually; the binding constraint is what the investor will tolerate across a long bull market |
| Institutional tail program (deep OTM)    | 1.5–2.5%               | Deep OTM ladder bought systematically; carry is budgeted as an insurance premium rather than judged year by year                                 |
| Institutional (richer / closer-to-money) | 3–5%+                  | Strikes sit closer to spot, or notional is larger; buys protection against shallower declines at proportionally higher cost                      |

The structural driver is strike distance. The further out of the money the ladder sits, the cheaper the program and the deeper the decline it needs before it pays anything. Moving the ladder toward spot raises the budget into the upper band and shortens the crash it protects against — the same trade-off as [Convexity Budget and Premium Budget](convexity-budget-and-premium-budget.md).

Many family offices treat 1% per year as a practical ceiling given performance sensitivity to carry. The 1–3% range used as the institutional target above is defensible for that investor type, but a program should be calibrated to what the investor and their stakeholders will sustain across a multi-year bull market without abandoning it. A program abandoned in year four has paid its full premium and delivered none of its protection.

!!! note

    These bands describe observed practice across program types, not a survey
    result. No public survey of family offices reports hedging premium as a
    percentage of AUM, so the figures should be read as a range of common
    practice rather than a measured distribution.

## Dynamic Calibration to the Volatility Regime

Strike selection and hedge sizing do not need to be static. A regime-sensitive approach:

| Vol Regime | Skew Percentile | Recommended Adjustment                                         |
| ---------- | --------------- | -------------------------------------------------------------- |
| VIX < 15   | < 30%           | Increase allocation; consider slightly closer-to-money strikes |
| VIX < 15   | > 50%           | Buy standard deep OTM; avoid chasing expensive skew            |
| VIX 15–25  | < 40%           | Maintain program as designed                                   |
| VIX > 25   | > 70%           | Reduce new purchases; wait for vol to normalize                |

This is consistent with the See [Tail Hedge Decision Matrix](../part-10/tail-hedge-decision-matrix.md) in PART X.
