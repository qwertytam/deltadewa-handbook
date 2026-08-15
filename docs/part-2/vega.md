---
title: "Vega (ν)"
---

Vega measures sensitivity of the option price to volatility.

It tells the investor how much the option price changes if implied volatility changes by 1 percentage point.

*Example:* “Long puts gain when vol spikes.”

If:

```text
vega = 0.50
```

Then:

```text
IV increases from 20% → 21%
```

Option price increases:

```text
$0.50
```

!!! note

    In many option models vega is defined per unit volatility change ($\Delta\sigma = 1.00$). Traders typically quote vega per 1 volatility point ($\Delta\sigma = 0.01$).

## Algebraic Definition for Vega

$\nu = \frac{\partial V}{\partial \sigma}$

## Black-Scholes expression for Vega

$\nu = S e^{-qT} \sqrt{T} N'(d_1)$

## Practical Interpretation for Vega

Vega measures exposure to volatility.

Long options:
> positive vega

Short options:
> negative vega

Important properties:

- larger for long maturity
- larger ATM

High vega:

```text
benefits strongly from panic
```

Low vega:

```text
price move helps but vol spike doesn't
```
