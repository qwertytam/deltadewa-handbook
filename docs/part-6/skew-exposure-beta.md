---
title: "Skew Exposure / Beta"
---

As described in Part III, See volatility skew reflects the higher implied volatility of downside strikes.

While skew describes the **shape of the volatility surface**, tail hedges also differ in how sensitive they are to changes in that surface.

This sensitivity is called **skew exposure or skew beta**.

Deep OTM puts typically have positive skew beta, meaning their implied volatility tends to rise faster than ATM volatility during market stress.

#### Definition of Skew Exposure / Beta

Skew beta measures how much the hedge value changes when downside skew steepens.

Formally:

$\text{Skew Beta} = \frac{\partial V}{\partial \text{Skew}}$

Where:

- $V$ = hedge value
- $Skew$ = difference between OTM put volatility and ATM volatility

#### Why Skew Beta Matters

During equity market crises, several things usually happen simultaneously:

```text
equity prices fall
implied volatility rises
downside skew steepens
```

Lower strikes often experience **larger volatility increases** than ATM options.

Example:

| Option type        | Before crisis | During crisis |
| ------------------ | ------------- | ------------- |
| ATM vol            | 20%           | 30%           |
| 25$\Delta$ put vol | 27%           | 38%           |

Because deeper OTM options experience larger volatility increases, hedges that hold those strikes benefit more. Deep OTM options typically have higher skew beta than ATM options.

#### Skew Beta Across Hedge Structures

Hedges have higher skew exposure when they hold:

```text
deeper OTM strikes
longer maturities
more tail-focused structures
```

Different hedges have different skew exposure:

| Structure            | Skew beta |
| -------------------- | --------- |
| ATM puts             | low       |
| moderately OTM puts  | moderate  |
| deep OTM tail hedges | high      |

Tail-hedge programs often deliberately include **deep OTM strikes** because they provide strong skew beta during crises.

However, these options may produce little protection during moderate drawdowns.

As a result, many programs combine multiple strikes to balance:

```text
delta protection
vega exposure
skew beta
carry cost
```

#### Important Distinction

Skew exposure should **not be confused with skew level**.

A hedge may have strong skew beta even when skew is expensive.

Similarly:

```text
cheap skew does not guarantee strong skew exposure
```

Those are two different dimensions.

#### Skew Convexity (Crisis Amplification of Skew Beta)

Skew convexity measures how much additional value a hedge gains when **downside skew steepens sharply during a crisis** — beyond what can be explained by the spot price falling or overall implied volatility rising.

In a typical equity market crash, three effects occur simultaneously:

| Effect          | What drives it                  | Captured by               |
| --------------- | ------------------------------- | ------------------------- |
| Price decline   | Spot falls                      | Delta (all put hedges)    |
| Vol spike       | Overall IV rises                | Vega (long options)       |
| Skew steepening | OTM puts rerate relative to ATM | Skew convexity (deep OTM) |

Deep OTM puts experience disproportionately larger volatility increases than ATM puts during a panic. A hedge concentrated in those strikes benefits from all three effects. A hedge positioned closer to ATM captures mainly the first two.

Some hedge structures appear effective when modeled using parallel volatility shifts, but perform poorly in real crises because actual volatility surfaces reprice with steepening skew rather than parallel shifts. This distinction matters most when comparing ATM or slightly OTM hedges against deeper OTM crash structures.

Monitoring skew convexity helps investors understand whether the hedge will benefit from the **full volatility surface repricing** that usually occurs during market crashes.

##### Key distinctions

These three concepts are often confused:

- Skew level — how expensive downside puts are today
- Skew beta — how sensitive the hedge is to small changes in skew
- Skew convexity — the additional, non-linear payoff produced by crisis-driven skew steepening

##### What This Means for Hedge Design

Skew convexity is an implicit property of the hedge structure, not typically tracked as a standalone dashboard metric. Programs that hold deep OTM strikes (30 to 40% OTM) with long maturities naturally have high skew convexity. Programs positioned nearer ATM have less, and may underperform their modelled payoffs in a genuine panic precisely because the model assumed parallel volatility shifts rather than the steep skew repricing that actually occurs.

The practical takeaway: **owning deep strikes is the primary mechanism for capturing skew convexity** — the crash scenario table will reflect it automatically if the ladder is structured correctly.

##### Skew Convexity as a Metric

In practice, many institutional dashboards do not track skew convexity explicitly. Instead they monitor:

- skew level or skew percentile
- strike distribution of the hedge
- skew exposure (skew beta)

These implicitly determine skew convexity.

##### Skew Convexity in Planning Scenarios

A practical way to evaluate skew convexity is through surface shock scenarios.

Example scenario:

```text
ATM volatility:      20% → 26%
25Δ put volatility:  27% → 38%
```

The increase in hedge value produced specifically by the larger volatility change in lower strikes represents skew convexity.

