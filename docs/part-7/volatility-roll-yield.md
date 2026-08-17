---
title: "Volatility Roll Yield"
---

## What It Is

When a long-dated option is held over time, its implied volatility changes not only because the overall level of the vol surface changes, but also because the option's remaining maturity shortens — causing it to slide along the vol term structure toward the shorter-dated part of the curve. [[Bennett 2014]](../footnotes/index.md#bennett), [[Sinclair 2013]](../footnotes/index.md#sinclair), [[Cboe: VIX Term Structure]](../footnotes/index.md#cboe-vix-term-structures)

The P&L effect of this slide is called *volatility roll yield*. It is a distinct cost or benefit that exists independently of:

- Theta (time value decay at fixed vol)
- Vega (P&L from changes in the overall level of implied volatility)

It is analogous to the roll yield in futures markets, where a futures position generates P&L simply from the passage of time as the contract rolls toward spot.

## How Term Structure Shape Determines the Sign

The direction of the effect depends entirely on the shape of the volatility term structure.

### Case 1 — Normal (upward sloping) term structure

In normal market conditions, longer-dated options trade at higher implied vol than shorter-dated options:

```text
3-month vol:  18%
12-month vol: 21%
24-month vol: 23%
```

A long 24-month put purchased at 23% vol will, all else equal, roll toward the 21% level as it approaches 12-month maturity. This produces a **headwind** — the option loses implied vol from term structure alone, before any theta decay is counted.

### Case 2 — Inverted (downward sloping) term structure

During market stress or crisis, short-dated vol typically surges above long-dated vol:

```text
3-month vol:  55%
12-month vol: 35%
24-month vol: 28%
```

In this environment, a long 24-month put rolling toward 12-month maturity gains implied vol — a **tailwind**. This is one of the reasons long-dated hedges can appear cheaper to hold on a carry basis during stress than simple theta would suggest.

## Quantifying the Effect

An approximate estimate of roll yield per roll period can be derived from the forward variance framework:

$\text{Vol Roll Yield} \approx \sigma_{current\ maturity} - \sigma_{new\ maturity}$

where $\sigma_{new\ maturity}$ is the implied vol at the option's maturity after the roll horizon.

A more precise estimate uses forward variance:

$\sigma_{fwd}^2 = \frac{T_2\sigma_2^2 - T_1\sigma_1^2}{T_2 - T_1}$

If the forward vol exceeds the spot vol for the target tenor, rolling generates a cost. If forward vol is below spot vol, rolling provides a benefit.

See [Forward Variance Level](../part-6/forward-variance-level.md) for the full definition.

## Practical Impact on a Tail Hedge Program

For a systematic long-dated put program (e.g., 18-month puts rolled at 9 to 12 months remaining), the total carry cost over time is not just theta. It includes:

```text
Total carry = Theta decay
            + Volatility roll yield (positive or negative)
            + Transaction costs (bid-ask spread on roll)
```

In a persistently normal (upward-sloping) term structure, roll yield is an additional headwind that is often underestimated when carry is measured using theta alone. In a historical backtest, this distinction matters: a theta-only carry estimate will overstate hedge affordability in low-vol, upward-sloping regimes.

## Rule of Thumb

When the term structure is steeply upward sloping, a program's realized carry will be modestly higher than theta suggests. When the term structure is flat or inverted, realized carry may be lower than theta suggests — or even negative in a crisis inversion.

## Practical Implication for Roll Timing

Programs that roll at fixed time intervals (e.g., roll at 9 months remaining) can reduce negative roll yield by:

1. **Rolling when the term structure is flatter** — less vol is given up moving from long to medium maturity
2. **Comparing the roll cost explicitly** before each roll, rather than rolling mechanically
3. **Monitoring the forward variance** to understand whether the expected volatility for the new position period is cheap or expensive relative to history

## Hedge Cost Implications

Volatility roll yield is a second-order cost relative to theta for most family office programs. It becomes more material in two specific cases — when the program is large relative to available liquidity (increasing effective transaction costs), and when the term structure is steeply upward sloping for an extended period, which has been the norm during low-volatility regimes like 2013 to 2017 and 2019. Ignoring it does not make the program unworkable, but it causes carry estimates to be systematically optimistic in the very regimes (low vol, steep term structure) where the program is supposed to be cheapest to run.

## Roll Friction and Bid-Ask Spread Costs

Beyond roll yield, the bid-ask spread on deep OTM long-dated options represents a real transaction cost that is easily underestimated. Unlike near-the-money front-month options, 30–40% OTM puts with 18-month maturities can trade with spreads of 5–10% of the mid-price or wider in quiet markets, and substantially wider during stress.

The full transaction cost of a roll includes:

```text
Total roll cost = Volatility roll yield (negative or positive)
               + Bid-ask spread on the sale of the existing position
               + Bid-ask spread on the purchase of the new position
               + Any market impact from size
```

For a \$10M portfolio running a 2% carry budget, a 5% bid-ask spread on both legs of a roll translates to roughly 10 basis points of additional cost per roll. Across four rolls per year this amounts to approximately 0.4% of portfolio value in friction — not negligible relative to a 2% budget.

**Mitigation:** execute rolls patiently using limit orders placed near the mid-price rather than hitting the bid or lifting the offer. In liquid SPX strikes, a mid-price limit order typically fills within the session. See [Execution Best Practices](program-constraints-and-governance.md#execution-best-practices-for-deep-otm-and-long-dated-options) in PART VII for further detail.
