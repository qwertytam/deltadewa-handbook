---
title: "Portfolio Hedge Sizing Framework"
---

A key decision in any hedge program is **how much protection to buy relative to the portfolio size**.

Professional investors typically think about hedge sizing using:

```text
portfolio volatility
drawdown tolerance
hedge convexity
carry budget
```

## Drawdown Protection Model

Let:

```text
P = portfolio value
H = hedge payoff
D = market drawdown
```

The net portfolio loss becomes:

```text
Net Loss = (P × D) + H
```

Example:

```text
Portfolio = $10M
Market drawdown = −25%
Equity loss = −$2.5M
Hedge payoff = $1.5M
Net loss = −$1.0M
```

The hedge reduced the drawdown from **25% to 10%**.

## Hedge Notional Guidelines

Institutional programs often target:

| Hedge Notional Relative to Portfolio | Description        |
| ------------------------------------ | ------------------ |
| 25 to 50%                            | partial protection |
| 50 to 75%                            | moderate hedge     |
| 75 to 100%                           | strong protection  |

Many tail-risk funds operate around:

```text
60 to 80% notional protection
```

because convexity amplifies hedge payoff in extreme scenarios. Said another way, convexity means hedge notional does not need to equal portfolio value.

## Sizing to the Risk Budget

A systematic approach to determining optimal hedge size:

**Step 1: Define the target maximum drawdown.**
Example: the investor targets a maximum portfolio drawdown of 20% even in a severe market crash.

**Step 2: Estimate unhedged drawdown in the target crash scenario.**
Example: in a −35% market crash, a portfolio with beta 1.0 loses approximately 35%.

**Step 3: Determine required hedge offset.**
The hedge must offset 35% − 20% = **15% of portfolio value**. On a \$10M
portfolio that is a required hedge gain of \$1.5M in the crash scenario.

**Step 4: Size the hedge to deliver the required offset.**

Sizing needs a payoff rate quoted *per dollar of hedge*, so the divisor is
[Crash Payoff per Unit of Notional](../part-6/ratio-disambiguation.md#crash-payoff-per-unit-of-notional)
— the hedge's crash gain over its notional. The crash payoff ratio will not
serve here: its denominator is the portfolio's equity loss, so it describes how
much of the loss a hedge absorbs and says nothing about how large the hedge is.

$$\text{Hedge Notional} = \frac{\text{Required Portfolio Offset} \times \text{Portfolio Value}}{\text{Crash Payoff per Unit of Notional}}$$

Example:

```text
Required portfolio offset            = 15% of $10M = $1.5M
Crash payoff per unit of notional
  at -35% SPX                        = 25%
Hedge Notional = $1.5M / 25%         = $6M = 60% of portfolio
```

The arithmetic closes in both directions: \$6M of notional paying 25% of
notional in the crash returns \$1.5M, which is the 15% of portfolio value Step 3
requires. Both sides of the division are now denominated in dollars of hedge.

!!! note "The same hedge read as a crash payoff ratio"

    Expressed as a
    [Crash Payoff Ratio](../part-6/crash-payoff-ratio-tail-hedge-effectiveness.md),
    this hedge returns \$1.5M against \$3.5M of equity loss — a 43% offset.
    The 40 to 80% band in
    [Typical Hedge Program Targets](typical-hedge-program-targets.md#typical-institutional-targets)
    is quoted at −25% SPX and this example at −35%, so the two are not
    comparable and 43% landing inside that numeric range is a coincidence
    rather than a pass. The hedge's gain is convex in the move while the
    portfolio's loss is linear, so the ratio rises with crash depth: the same
    book read at −25% gives a different figure, and that is the one to check
    against the band. A crash payoff ratio quoted without its scenario cannot
    be read against any band at all.

**Step 5: Check carry cost.**
Confirm the premium spend implied by the hedge notional is within the annual carry budget. If it exceeds the budget, reduce hedge notional or shift to deeper OTM strikes to reduce cost.

This five-step process ties hedge sizing directly to the investor's stated loss tolerance rather than to an arbitrary percentage of premium spend.
