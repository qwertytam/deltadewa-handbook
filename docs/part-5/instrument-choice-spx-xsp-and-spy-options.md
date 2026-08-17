---
title: "Instrument Choice: SPX, XSP, and SPY Options"
---

When implementing a long-equity downside hedge program, the choice of **underlying option instrument** matters for:

- execution efficiency
- tax treatment
- assignment risk
- position sizing
- operational simplicity

Institutional tail-hedge programs most commonly use **index options**, particularly SPX.

## SPX Options (S&P 500 Index Options)

SPX options are typically the preferred instrument for institutional downside hedging.

Key characteristics:

| Feature            | Description                                        |
| ------------------ | -------------------------------------------------- |
| Settlement         | Cash settled                                       |
| Settlement timing  | AM for standard monthlies; PM for SPXW Weeklys/EOM |
| Exercise style     | European                                           |
| Underlying         | S&P 500 index                                      |
| Contract size      | Large notional                                     |
| Tax treatment (US) | Section 1256 (60/40 treatment)                     |

Advantages:

- **No assignment risk** due to European exercise
- **Cash settlement** simplifies position management
- **Highly liquid institutional market**
- Efficient for **large portfolio hedging**

Because there is no physical delivery of shares, SPX options avoid complications associated with assignment or early exercise.

As a result, **most institutional tail-hedge funds implement crash protection using SPX options.**

## XSP Options (Mini SPX)

XSP options track the same S&P 500 index but at **1/10 the size of SPX**.

| Feature           | Description                          |
| ----------------- | ------------------------------------ |
| Settlement        | Cash settled                         |
| Settlement timing | PM — official closing level of index |
| Exercise style    | European                             |
| Contract size     | ~1/10 SPX                            |

Advantages:

- Allows **finer position sizing**
- Useful for **smaller portfolios**
- Maintains the **same cash settlement and European exercise as SPX**

One structural difference is worth noting rather than assuming away: every XSP
series is **PM-settled**, whereas the standard monthly SPX contract is
AM-settled against the opening rotation. An XSP position therefore trades right
up to the close that determines its settlement value, and does not raise the
overnight-gap question that standard SPX series do. See
[Settlement Mechanics](../part-1/exercise-settlement.md#settlement-mechanics).

XSP is often used by investors who want index-style hedging but require **more granular hedge sizing**.

!!! note

    While XSP tracks the same underlying as SPX, its options market is smaller. Bid-ask spreads and open interest in XSP can be thinner than in SPX, particularly for deep OTM and long-dated strikes. Investors should check OI and recent volume at target strikes before committing to XSP for large notional trades, and should use limit orders to avoid paying inflated spreads. Using XSP requires execution patience. A quoted spread of a given size is a larger fraction of the premium on a contract one-tenth the notional, so the comparison that matters between SPX and XSP is execution cost per unit of exposure, not the quoted tick itself.

## SPY Options (ETF Options)

SPY options are based on the **SPDR S&P 500 ETF** rather than the index.

| Feature           | Description                    |
| ----------------- | ------------------------------ |
| Settlement        | Physical                       |
| Settlement timing | PM, on the expiration date     |
| Exercise style    | American                       |
| Underlying        | SPY ETF                        |

Key differences:

- **American exercise introduces assignment risk**
- Deep ITM options may be exercised early
- Positions can result in **delivery of ETF shares**

Settlement timing means something different here. Because SPY options are
American, they can be exercised on any business day, so "PM" describes only what
happens to a contract still open at the expiration close — not a single
scheduled settlement event of the kind SET represents for AM-settled index
series [[Cboe: Settlement Style]](../footnotes/index.md#cboe-settlement-style).

Despite these limitations, SPY options are extremely liquid and may be preferred when:

- smaller trade sizes are required
- tighter spreads are available
- access to index options is restricted

However, because of the assignment risk and operational complexity, **SPY is usually not the first choice for systematic tail-hedging programs.**

## Practical Rule of Thumb

Typical preference hierarchy for institutional hedging:

```text
SPX → preferred for institutional programs
XSP → useful for smaller portfolios or fine sizing
SPY → acceptable but operationally more complex
```
