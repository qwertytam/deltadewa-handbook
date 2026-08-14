---
title: "Rho (ρ)"
---

Rho measures sensitivity of the option price to interest rates.

*Example:* “Long-dated put hedges have negative rho — they benefit when rates fall.”

If:

```text
rho = 0.20
```

Then:

```text
rates increase by 1%
```

Option value increases:

```text
For a call +$0.20 → long calls have positive rho, increasing in value when interest rates rise
For a put -$0.20 → long puts have negative rho, decreasing in value when interest rates rise
```

Note: During equity crises, interest rates often fall due to monetary policy responses, leading to long-dated put hedges increasing in value.

#### Algebraic Definition Rho

$\rho = \frac{\partial V}{\partial r}$

#### Practical Interpretation Of Rho

Rho matters most for:

- Long-dated options
- Deep ITM calls

Rho sensitivity depends primarily on:

- maturity
- interest rates
- dividends
- forward pricing

#### Rho in Non-Standard Rate Scenarios

The standard assumption embedded in tail-hedging frameworks is that equity crises are accompanied by rate cuts, which produce a rho tailwind for long put holders (rates fall → put value rises). This assumption held in 2001, 2008, and 2020.

In a **stagflationary scenario** — where inflation is elevated and the central bank cannot or does not cut rates during an equity drawdown — this tailwind disappears. The hedge must then rely entirely on delta, gamma, and vega. For a long-dated OTM put in a rising-rate environment, the rho headwind can partially offset gains from price decline, reducing hedge effectiveness relative to a standard crisis scenario.

This is a second-order effect for most crash scenarios, but investors hedging in a high-rate environment should be aware that the rho benefit embedded in historical hedge analyses may not repeat.

