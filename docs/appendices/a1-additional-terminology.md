---
title: "A1 Additional Terminology"
---

Terms a reader is likely to meet in passing. Where a term has a full treatment
in one of the Parts, the entry below says what it means and points there rather
than repeating the explanation.

## Covered Call

Short call against long stock.

*Example:* “Generate income while holding shares.”

## Straddle

Buy call + put same strike.

*Example:* “Bet on big move either direction.”

!!! note

    This is more of a volatility strategy rather than downside hedging.

## Strangle

OTM call + OTM put.

*Example:* “Cheaper volatility bet.”

!!! note

    This is more of a volatility strategy rather than downside hedging.

## Calendar Spread

Same strike, different expiries.

*Example:* Sell front-month, buy longer-dated.

## Pin Risk

Pin risk occurs when the underlying closes **very close to a strike price at expiration**.

*Example:* “Avoid pin risk into expiration.”

```text
stock = 100
strike = 100
```

!!! note

    This is relevant mainly to short options or expiry trading. Not important for long-dated tail hedges.

## Gamma Scalping

Gamma scalping is a trading strategy that profits from volatility.

1. buy options (long gamma)
2. hedge delta dynamically

When price moves:

```text
buy low
sell high
```

This captures realized volatility.

!!! note

    This is more relevant to market making or volatility trading, not portfolio hedging.

## IPS (Investment Policy Statement)

The governing document that states what a portfolio may and may not do. A hedge program's mandate, budget and constraints live in it.

*Example:* “The IPS caps annual hedge premium.”

See [Investment Policy Statement (IPS) Integration](../part-7/program-constraints-and-governance.md#investment-policy-statement-ips-integration).

## SET

The ticker under which the exchange publishes the settlement value of AM-settled SPX options — a Special Opening Quotation (SOQ) built from component opening prices, not the index's own opening level.

*Example:* “The contract settled against SET, not against Friday's open.”

See [SET and the Special Opening Quotation](../part-1/exercise-settlement.md#set-and-the-special-opening-quotation).

## AM and PM Settlement

Whether an option's settlement value is struck from opening prices on the expiration morning or from closing prices on the expiration date. Standard monthly SPX contracts are AM-settled; SPXW and XSP are PM-settled.

*Example:* “Check the settlement flavour before holding into expiration.”

See [AM and PM Settled Series](../part-1/exercise-settlement.md#am-and-pm-settled-series).

## SPXW

The ticker root for Cboe's PM-settled S&P 500 index option series — the Weeklys and the end-of-month contracts — as distinct from the standard AM-settled monthly.

*Example:* “Rolled into an SPXW series to avoid AM settlement.”

## Reg T

Shorthand for Regulation T. For exchange-listed options it does not set the margin amount itself; it defers to the exchange and SRO rules, which apply a separate formula to each recognised position type.

*Example:* “Under Reg T rules the debit spread is simply paid for in full.”

See [Strategy-Based Margin](../part-5/running-structures-with-sold-legs.md#strategy-based-margin).

## Portfolio Margin

A margin regime that computes the requirement by revaluing positions across a range of hypothetical market moves, rather than by applying a formula to each position type.

*Example:* “Under portfolio margin the offsetting legs are recognised.”

See [Portfolio Margin](../part-5/running-structures-with-sold-legs.md#portfolio-margin).

## Buying Power

The capital an account has available to open new positions. A sold option consumes it for as long as the position stays open, and it is returned when the position closes.

*Example:* “The short leg ties up buying power all year.”

See [How a Sold Leg Consumes Buying Power](../part-5/running-structures-with-sold-legs.md#how-a-sold-leg-consumes-buying-power).

## Legging In

Working each leg of a multi-leg structure as its own order, rather than sending the structure as one order at a net price.

*Example:* “Legged into the spread and got caught by the second leg.”

See [Executing the Legs](../part-5/running-structures-with-sold-legs.md#executing-the-legs).

## Monetization

Realising a hedge's gain by closing or reducing it, as opposed to holding it to expiration.

*Example:* “Monetized a third of the position at −20%.”

See [Monetization Philosophy](../part-8/monetization-philosophy.md).

## 25-Delta Risk Reversal

A measure of skew: the implied volatility of the 25-delta put less that of the 25-delta call.

*Example:* “The 25-delta risk reversal widened into the sell-off.”

See [Practical Skew Metrics](../part-3/volatility-skew.md#practical-skew-metrics).

## SKEW Index

A Cboe-published index derived from the risk-neutral skewness of the 30-day S&P
500 log-return distribution, computed from a strip of out-of-the-money SPX
options. A reading of 100 corresponds to a normal distribution; higher readings
mean more negative tail skew. Distinct from a [25-Delta Risk
Reversal](#25-delta-risk-reversal), which is a two-strike volatility spread
computed in-house rather than a published index.

*Example:* “SKEW held above 140 while the risk reversal barely moved.”

See [Two Different Measures Called "Skew"](../part-3/volatility-skew.md#two-different-measures-called-skew).

## Skew Percentile

The rank of the current skew reading against its own history, expressed as a
percentage. It says whether crash protection is cheap or expensive *relative to
the past*, not whether it is cheap in absolute terms. A percentile is
uninterpretable without two accompanying facts: which skew measure was ranked,
and over what lookback window.

*Example:* “Skew percentile of 22% on a trailing five-year window — protection
is historically cheap.”

See [The Lookback Window](../part-3/volatility-skew.md#the-lookback-window).
