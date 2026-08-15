---
title: "A1 Additional Terminology"
---

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
