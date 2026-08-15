---
title: "A2 Mathematical Formula"
---

## Black–Scholes Option Pricing

Call option price:

$V = S e^{-qT} N(d_1) − K e^{-rT} N(d_2)$

Put option price:

$V = K e^{-rT} N(-d_2) - S e^{-qT} N(-d_1)$

Where:

$d_1 = \frac{ln(S/K) + (r − q + \frac{1}{2}\sigma^2)T} { \sigma \sqrt{T} }$

$d_2 = d_1 − \sigma \sqrt{T}$

Variables:

| Symbol   | Meaning          |
| -------- | ---------------- |
| $S$      | underlying price |
| $K$      | strike           |
| $T$      | time to maturity |
| $\sigma$ | volatility       |
| $r$      | risk‑free rate   |
| $q$      | dividend yield   |

## Greeks Summary

| w.r.t.                | 1st derivative                                       | 2nd                                                                                                                                                                         | 3rd                                                                                                                                          |
| --------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Underlying price: $S$ | $\Delta = \frac{\partial V}{\partial S}$             | $\Gamma = \frac{\partial \Delta}{\partial S} = \frac{\partial^2 V}{\partial S^2}$                                                                                           | $Speed = \frac{\partial \Gamma}{\partial S} = \frac{\partial^3 V}{\partial S^3}$                                                             |
| Price and Volatility  |                                                      | $Vanna = \frac{\partial \Delta}{\partial \sigma} = \frac{\partial \nu}{\partial S} = \frac{\partial^2 V}{\partial S\ \partial \sigma}$                                      | $Zomma = \frac{\partial \Gamma}{\partial \sigma} = \frac {\partial Vanna}{\partial S} = \frac {\partial^3 V}{\partial S^2\ \partial \sigma}$ |
| Volatility: $\sigma$  | Vega: $\nu = \frac{\partial V}{\partial \sigma}$     | $\text{Vomma}={\frac {\partial \nu}{\partial \sigma }} = \frac {\partial ^{2}V}{\partial \sigma ^{2}}$                                                                      | $Ultima = \frac{\partial Vomma}{\partial \sigma} = \frac{\partial^3 V}{\partial \sigma^3}$                                                   |
| Volatility and Time   |                                                      | $Veta = \frac{\partial \nu}{\partial \tau} = \frac{\partial^2 V}{\partial \sigma\ \partial \tau}$                                                                           |                                                                                                                                              |
| Time: $t$             | $\Theta = -\frac{\partial V}{\partial t}$            | $Charm = \frac{\partial \Delta}{\partial t} = -\frac{\partial \Delta}{\partial \tau} = \frac{\partial \Theta}{\partial S} = \frac{\partial^2 V}{\partial \tau\ \partial S}$ |                                                                                                                                              |
| Interest rate: $r$    | $\rho = \frac{\partial V}{\partial r}$               | $Vera = \frac{\partial \rho}{\partial \sigma} = \frac{\partial^2 V}{\partial \sigma\ \partial r}$                                                                           |                                                                                                                                              |
| Dividend yield: $q$   | $\epsilon\ or\ \psi = \frac{\partial V}{\partial q}$ |                                                                                                                                                                             |                                                                                                                                              |

Notes:

- See [Charm](../part-2/charm.md) for differences between $t$ and $\tau$

## Greeks Interpretation Summary

| Greek    | Range    | Factor           |
| -------- | -------- | ---------------- |
| $\Delta$ | -1 to +1 | Underlying Price |
| $\Gamma$ | 0 to +1  | Delta            |
| $\Theta$ | < 0      | Time             |
| $\nu$    | Varies   | Volatility       |
| $\rho$   | Varies   | Interest Rate    |

### Delta

| Value           | Moneyness     | Interpretation                                                              | Example                     |
| --------------- | ------------- | --------------------------------------------------------------------------- | --------------------------- |
| ~+0.80 to +1.00 | Deep ITM call | Moves nearly dollar-for-dollar *with* the stock                             | \$150 call on a \$195 stock |
| ~+0.50          | ATM call      | Gains ~\$0.50 for each \$1 stock increase                                   | \$195 call on a \$195 stock |
| ~+0.05 to +0.20 | OTM call      | Low sensitivity; small chance of finishing ITM                              | \$230 call on a \$195 stock |
| ~-0.05 to -0.20 | OTM put       | Low sensitivity; stock would need to fall significantly to reach the strike | \$160 put on a \$195 stock  |
| ~-0.50          | ATM put       | Loses ~\$0.50 for each \$1 stock increase                                   | \$195 put on a \$195 stock  |
| ~-0.80 to -1.00 | Deep ITM put  | Moves nearly dollar-for-dollar *against* the stock                          | \$240 put on a \$195 stock  |

!!! note

    Delta is a continuous value - these ranges are guidelines, not fixed buckets. See discussions on See [the Greeks](../part-2/index.md) for a fuller explanation on drivers of moneyness.
