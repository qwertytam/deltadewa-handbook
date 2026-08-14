---
title: "Beta-Adjusted Hedge Sizing"
---

A long-only equity portfolio with a mix of holdings rarely has a beta of exactly 1.0 to the SPX. If the portfolio has a beta of 0.85 to the S&P 500, buying SPX puts sized to 100% notional overhedges the market risk by roughly 15%.

Standard institutional practice is to beta-adjust the hedge sizing as follows:

$\text{Hedge Notional} = \text{Portfolio Value} \times \beta_{portfolio/SPX}$

\$N_{contracts​}=\frac{\text{Hedge Notional​}}{SPX \times \text{Contract Multiplier}}$

where:

- $\text{Contract Multiplier}$ is typically 100

Note: Portfolio beta should be recalculated at least annually, or whenever significant portfolio changes occur — for example, when positions representing more than 10% of portfolio value are added or removed. Beta drift of 0.10 or more warrants resizing the hedge at the next scheduled roll to avoid persistent over- or under-hedging. A portfolio that shifts toward more defensive names over time (beta drifts from 1.00 to 0.85) with an unchanged hedge notional is overhedged by approximately 18%, paying unnecessary carry for protection that exceeds the actual market exposure.

#### Worked Example — Multi-Position Portfolio

A portfolio holds the following positions:

| Position               | Value    | Beta vs SPX |
| ---------------------- | -------- | ----------- |
| Large-cap US equities  | \$6M      | 1.05        |
| Mid-cap US equities    | \$2M      | 1.15        |
| International equities | \$2M      | 0.70        |
| **Total**              | **\$10M** |             |

Weighted portfolio beta:

$\beta_{portfolio} = \frac{(6M \times 1.05) + (2M \times 1.15) + (2M \times 0.70)}{10M} = \frac{6.30M + 2.30M + 1.40M}{10M} = 1.00$

Hedge notional = \$10M × 1.00 = \$10M

At SPX = 5,000, each SPX contract covers: \$5,000 × 100 = \$500,000 notional.

\$N_{SPX} = \frac{\$10M}{\$500{,}000} = 20 \ \text{SPX contracts}$

If using XSP (1/10 the size):

\$N_{XSP} = 20 \times 10 = 200 \ \text{XSP contracts}$

If portfolio beta were instead 0.85, the hedge notional would be \$8.5M, requiring only 17 SPX contracts. Buying 20 contracts in that case would overhedge by approximately 18% — a meaningful structural error in a systematic program.

#### XSP Strike Ladder Distribution

For investors using XSP for finer granularity, the 200 XSP contracts computed above would be distributed across a strike ladder and maturity buckets as follows. Using the standard 3-strike, 2-maturity allocation:

Strike allocations (consistent with See the typical tail hedge structure):

| Strike  | Allocation % | XSP Contracts | Notional |
| ------- | ------------ | ------------- | -------- |
| 20% OTM | 35%          | 70            | \$3.5M    |
| 30% OTM | 40%          | 80            | \$4.0M    |
| 40% OTM | 25%          | 50            | \$2.5M    |

Split across two maturity buckets (e.g., 12 months and 18 months, weighted 40% / 60%):

| Strike    | 12-month XSP | 18-month XSP |
| --------- | ------------ | ------------ |
| 20% OTM   | 28           | 42           |
| 30% OTM   | 32           | 48           |
| 40% OTM   | 20           | 30           |
| **Total** | **80**       | **120**      |

This structure gives 200 XSP contracts total distributed across six positions, each sized to approximately \$400k–\$700k notional — fine enough granularity to adjust individual legs without large step changes in exposure.

