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

#### Drawdown Protection Model

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

#### Hedge Notional Guidelines

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

#### Sizing to the Risk Budget

A systematic approach to determining optimal hedge size:

**Step 1: Define the target maximum drawdown.**
Example: the investor targets a maximum portfolio drawdown of 20% even in a severe market crash.

**Step 2: Estimate unhedged drawdown in the target crash scenario.**
Example: in a −35% market crash, a portfolio with beta 1.0 loses approximately 35%.

**Step 3: Determine required hedge offset.**
Hedge must offset: 35% − 20% = 15% of portfolio value.

**Step 4: Size the hedge to deliver the required offset.**

Using the crash payoff ratio:

$\text{Hedge Notional} = \frac{\text{Required Portfolio Offset}}{\text{Expected Crash Payoff Ratio}} \times \text{Portfolio Value}$

Example:

```text
Required portfolio offset = 15%
Expected crash payoff ratio at -35% = 25%
Hedge Notional = (15% / 25%) × $10M = $6M = 60% of portfolio
```

**Step 5: Check carry cost.**
Confirm the premium spend implied by the hedge notional is within the annual carry budget. If it exceeds the budget, reduce hedge notional or shift to deeper OTM strikes to reduce cost.

This five-step process ties hedge sizing directly to the investor's stated loss tolerance rather than to an arbitrary percentage of premium spend.

