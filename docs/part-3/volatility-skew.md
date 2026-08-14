---
title: "Volatility Skew"
---

#### Definition of Volatility Skew

In equity options markets, implied volatility varies across strikes.
This variation is called **volatility skew**.

Instead of all strikes having the same volatility (as assumed in Black-Scholes), the market typically prices **lower strikes with higher implied volatility** than higher strikes.

This produces the characteristic **downward-sloping skew curve**.

Example structure:

```text
OTM puts > ATM > OTM calls
```

This reflects demand for crash protection.

Graphically:

```text
vol
 ^
 |\
 | \
 |  \
 |
 +------ strike
```

Where:

- lower strikes correspond to **downside protection**
- higher strikes correspond to **upside optionality**

*Example:* “Equity puts have downside skew.”

#### Why Skew Exists

In equity markets, investors have strong demand for **downside protection**, particularly from:

- asset managers
- pension funds
- structured-product hedging
- portfolio insurance strategies

This persistent demand pushes up the price of OTM puts relative to other options, resulting in higher implied volatility for lower strikes.

As a result:

```text
OTM puts therefore trade at structurally higher implied volatility than ATM options.
```

#### Practical Skew Metrics

Traders rarely measure skew using raw strike derivatives.
Instead they use **delta-based metrics**, which are more stable across maturities.

A common definition is:

\$Skew = \sigma_{25\Delta\ put} - \sigma_{ATM}$

Where:

- \$25\Delta_{put} \approx 10\ to\ 15\% \text{ OTM}$

In practice traders often approximate ATM volatility using the 50$\Delta$ call
or the 40 to 50$\Delta$ put depending on convention.

Example:

| Strike         | IV  |
| -------------- | --- |
| ATM            | 20% |
| 25$\Delta$ put | 27% |

Result:

```text
Skew = 27 − 20 = 7 vol points
```

#### Interpretation of Volatility Skew

Skew represents the *market price of crash protection* aka *crash insurance*

When skew is:

Low
→ downside protection relatively cheap.

High
→ investors already paying large premiums for crash insurance.

Because skew varies through time, tail-hedge programs often track **skew percentiles** relative to historical ranges when deciding when to add or reduce protection.

#### Skew Percentile

Because skew varies over time, institutional desks often evaluate skew relative to history.

$\text{Skew Percentile}=\text{rank of current skew vs historical distribution}$

Example:

| Percentile | Interpretation                    |
| ---------- | --------------------------------- |
| < 20%      | protection historically cheap     |
| 20 to 70%  | normal                            |
| 70 to 80%  | moderately expensive              |
| 80 to 90%  | protection historically expensive |
| > 90%      | panic pricing                     |

Typical hedge dashboards display:

```text
Skew percentile (Last 5 to 10 years): 22%
Interpretation: protection cheap
```

Most institutional dashboards measure skew using a 25$\Delta$ risk reversal (25$\Delta$ put IV minus 25$\Delta$ call IV) or the difference between the 25$\Delta$ put and ATM volatility.

