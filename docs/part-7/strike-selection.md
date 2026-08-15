---
title: "Strike Selection"
---

The **“strike ladder” (multi-strike hedge) across downside skew** is one of the most important design choices in a long-term tail-hedging program. Almost every professional tail-hedge fund uses **multiple strikes instead of a single deep OTM put**, because it dramatically improves the **convexity-to-carry trade-off** and stabilizes the hedge across different crash sizes.

Strike ladder design is influenced by both skew level and skew slope. When **skew is steep**, deeper strikes become relatively more expensive and ladder weighting may shift slightly toward nearer strikes.

#### Why a Single-Strike Hedge Is Inefficient

Suppose the market is:

```text
SPX = 5000
```

A single deep OTM put has the following payoff profile:

```text
Strike = 3500  (30% OTM)
```

##### Payoff behavior

| SPX move | Put payoff     |
| -------- | -------------- |
| -10%     | almost nothing |
| -20%     | small          |
| -30%     | large          |
| -40%     | very large     |

The problem:

- hedge only activates in very large crashes
- moderate drawdowns remain largely unprotected

The investor ends up with **“gap risk” between protection layers**.

#### The Strike Ladder Concept

Instead of one strike, funds build **layers of protection across multiple strikes**.

Example ladder:

| Strike          | Allocation | Maturity  |
| --------------- | ---------- | --------- |
| 4000  (20% OTM) | 35%        | 18 months |
| 3500  (30% OTM) | 40%        | 18 months |
| 3000  (40% OTM) | 25%        | 18 months |

Each strike responds to **different crash severities**.

Why this weighting works:

- nearer strikes protect **moderate corrections**
- deeper strikes capture **crisis convexity**
- lower carry cost
- stronger skew beta
- massive convex payoff in crashes

##### How the Payoff Changes

| SPX move | 20% put  | 30% put | 40% put  |
| -------- | -------- | ------- | -------- |
| -10%     | small    | 0       | 0        |
| -20%     | moderate | small   | 0        |
| -30%     | large    | large   | moderate |
| -40%     | huge     | huge    | huge     |

Now the hedge works **across the entire crash spectrum**.

#### Why Funds Use Multiple Strikes

There are three primary reasons.

##### 1. Smoother hedge payoff

A ladder creates a **continuous convex payoff curve**.

Instead of:

```text
flat → explosive
```

The investor gets:

```text
small gain → medium gain → large gain
```

##### 2. Better skew exposure

OTM skew increases as strike decreases. Example typical SPX skew:

| Strike  | IV  |
| ------- | --- |
| ATM     | 20% |
| 20% OTM | 25% |
| 30% OTM | 28% |
| 40% OTM | 32% |

Deep strikes benefit **most from skew expansion during crashes**.

##### 3. Better carry efficiency

Different strikes have different theta.

*Example:*

| Strike  | Annual carry |
| ------- | ------------ |
| 20% OTM | high         |
| 30% OTM | medium       |
| 40% OTM | low          |

Blending them reduces overall carry cost.

#### Selecting Strikes

Most tail-hedge funds allocate across **three to five strikes using 20 to 40% OTM puts**.

See [example allocation ladder](#the-strike-ladder-concept).

