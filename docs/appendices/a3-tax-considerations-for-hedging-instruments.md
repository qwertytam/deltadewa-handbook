---
title: "A3 Tax Considerations for Hedging Instruments"
---

Different derivatives instruments have different tax treatments.

## SPX Index Options

Characteristics:

```text
European style
cash settled
Section 1256 treatment
```

Tax treatment in the United States:

```text
60% long-term capital gains
40% short-term capital gains
mark-to-market annually
```

## XSP Index Options

Same as See [SPX index options](#spx-index-options)

## SPY Options

Characteristics:

```text
American style
physically settled
```

Tax treatment:

```text
standard capital gains
holding period dependent
```

## Futures and Futures Options

Index futures and options on futures also typically fall under:

```text
Section 1256 taxation
```

Advantages:

```text
favorable tax treatment
high liquidity
low spreads
```

## Summary Comparison Table

| Instrument                     | Tax Treatment          | Section 1256? | Mark-to-Market at Year-End | Holding Period                 |
| ------------------------------ | ---------------------- | ------------- | -------------------------- | ------------------------------ |
| SPX puts                       | 60% LT / 40% ST        | Yes           | Yes                        | N/A (1256 rules override)      |
| XSP puts                       | 60% LT / 40% ST        | Yes           | Yes                        | N/A                            |
| SPY puts                       | Standard capital gains | No            | No                         | Based on actual holding period |
| VIX options                    | 60% LT / 40% ST        | Yes           | Yes                        | N/A                            |
| Single-stock puts              | Standard capital gains | No            | No                         | Based on actual holding period |
| E-mini S&P 500 futures options | 60% LT / 40% ST        | Yes           | Yes                        | N/A                            |

## Additional Tax Considerations

**Wash sale rules (Section 1091) — do not apply to Section 1256 contracts:** Section 1256(f)(5) provides that Section 1091 "shall not apply to any loss taken into account by reason of" the Section 1256 mark-to-market rule [[26 U.S.C. § 1256]](../footnotes/index.md#irc-1256). SPX and XSP puts, VIX options and options on index futures are nonequity options, and so Section 1256 contracts: Section 1256(g)(6) confines "equity option" to options on stock and on narrow-based security indices, which leaves a broad-based index option outside that definition. Rolling these at a loss therefore does not trigger a wash sale, however closely the replacement position resembles the one sold, and a roll schedule that generates consistent losses does not need to be designed around the 30-day window.

The rule does apply to instruments outside Section 1256. SPY puts and single-name equity puts are equity options taxed under the standard capital-gains regime, so selling one at a loss and acquiring a substantially identical option within 30 days before or after the sale defers the loss [[26 U.S.C. §§ 1091 and 1092]](../footnotes/index.md#irc-1091-1092). A program that holds these as secondary instruments needs its roll schedule checked against the wash sale window; one hedging solely with SPX or XSP does not.

**Straddle rules (Section 1092) — a separate regime:** Section 1092 is a different Code section from Section 1091 and is not switched off by Section 1256(f)(5). It defers a loss on one position to the extent of unrecognized gain on an offsetting position, so a hedge held against the equity portfolio it protects can raise mixed straddle questions even where wash sale rules do not reach it. This is a question about offsetting positions, not about repurchase timing, and the two should not be run together. Consult tax counsel on straddle identification and the mixed straddle elections before establishing a roll schedule.

**Constructive sale (Section 1259):** A collar that eliminates substantially all risk of loss and opportunity for gain on an appreciated equity position can be treated as a constructive sale, triggering gain recognition without an actual sale. Leaving meaningful upside exposure (call strike at least 10–15% OTM) generally avoids this treatment, but specific transactions require individual review.

**State tax treatment:** Section 1256 treatment applies at the federal level. State tax treatment of derivatives varies; some states do not conform to the 60/40 split and may tax all gains as ordinary income.

!!! warning "Not tax advice"

    All tax sections are for general orientation only. Specific treatment
    should be confirmed with qualified tax counsel before implementing any
    hedging strategy.
