---
title: "Program Constraints and Governance"
---

Before designing a systematic tail-hedging program, investors must define **structural constraints** that determine what types of hedges are feasible.

Even when two portfolios face the same market risks, their hedge designs may differ significantly depending on mandate restrictions.

The investment mandate for a family office may need to be explicitly amended to allow derivatives and short options before any program is implemented. A surprising number of family office mandates are drafted in terms of "long-only equities" and exclude derivatives without anyone having explicitly intended to do so. A CIO should verify mandate language before committing to a systematic hedging program.

Typical institutional constraints include:

## Allowed Instruments

Investment mandates often restrict which instruments can be used.

Examples:

- listed equity index options only
- no volatility derivatives
- no short options
- no futures

These restrictions may prevent the use of certain strategies such as:

- variance swaps
- VIX derivatives
- volatility carry overlays

As a result, many institutional investors implement tail hedges **using only long index puts**.

## Margin and Leverage Limits

Some portfolios face strict constraints on:

- margin usage
- gross exposure
- derivatives leverage

These constraints affect:

- hedge sizing
- strike selection
- whether spread structures are allowed

For example, if short options are prohibited, the program cannot use **put spreads or collars** to reduce carry cost.

## Liquidity and Execution Constraints

Operational considerations also matter.

Questions include:

- Can the hedge be **executed without significant market impact?**
- Can positions be **rolled efficiently at scale?**
- Are spreads acceptable during volatile markets?

Because crash periods often involve **extreme liquidity deterioration**, the hedge program should prioritize instruments with **deep and reliable liquidity.**

## Execution Best Practices for Deep OTM and Long-Dated Options

Deep OTM puts and long-dated options often have wider bid-ask spreads than near-the-money, front-month options. For a systematic program, cumulative transaction costs from poor execution can materially increase the effective carry cost.

Practical execution guidelines:

- **Use limit orders** rather than market orders for options with wide spreads. A limit order placed near the mid-price typically fills within the session for liquid strikes.
- **Stage entry** across multiple sessions for large notional trades (e.g., greater than \$5M notional in a single expiry). This reduces market impact.
- **Avoid executing immediately after large market moves**, when spreads widen and liquidity thins. For a systematic roll program, flexibility to delay roll execution by several sessions reduces transaction costs in stressed markets.
- **Monitor open interest and daily volume** at target strikes before executing. SPX 20–30% OTM puts with 12–18 month maturities typically have adequate institutional liquidity; 40% OTM strikes at 24 months can be thinly traded and may require larger spread concessions.
- **Work through an experienced options desk** rather than a retail platform for trades above \$1M notional.

## Governance and Rebalancing Authority

A successful hedge program requires clear governance rules defining:

- who has authority to monetize hedges
- how re-risk decisions are made
- how often the program is reviewed

Without predefined rules, investors may fail to monetize hedges during crises or may re-risk too quickly.

Most institutional programs therefore define **explicit monetization and re-risk frameworks before crises occur.**

## Investment Policy Statement (IPS) Integration

The hedge program should be explicitly documented in the Investment Policy Statement or equivalent governing document. An undocumented program is vulnerable to ad hoc modification under pressure — precisely when discipline matters most.

Minimum IPS provisions for a hedge program:

| Parameter              | Example                                                  |
| ---------------------- | -------------------------------------------------------- |
| Annual premium budget  | 1–2% of AUM                                              |
| Approved instruments   | Listed SPX / XSP puts only                               |
| Strike range           | 15–40% OTM                                               |
| Maturity range         | 12–24 months                                             |
| Roll trigger           | Maturity < 9 months remaining                            |
| Monetization authority | CIO or Investment Committee                              |
| Monetization triggers  | VIX > 40, SPX down > 15%, or hedge MTM > 5% of portfolio |
| Re-risk criteria       | VIX < 15, skew percentile < 30%                          |
| Review frequency       | Quarterly                                                |

Embedding these parameters in the IPS removes discretion from the decision framework during a crisis and ensures that governance does not become a bottleneck at the worst possible moment.

In addition to quarterly operational reviews, conduct a comprehensive annual review of the hedge program parameters themselves - including premium budget, strike range, maturity range, and monetization triggers - to ensure they remain aligned with the family's current risk tolerance, portfolio composition, and financial circumstances.

## Position Documentation and Counterparty Risk

Each option position should be documented with the underlying instrument and exchange, strike, maturity, notional, number of contracts, entry date, premium paid, and current mark-to-market.

For programs using a single prime broker, counterparty concentration risk should be considered. During a 2008-style liquidity crisis, broker operational capacity can become constrained. Where program size warrants it, distributing positions across two prime brokers reduces single-point-of-failure risk in execution, margining, and position access. For smaller programs, it is typically practical to only use *one* highly rated institutional broker, with a secondary cash/custody account elsewhere for emergency liquidity.
