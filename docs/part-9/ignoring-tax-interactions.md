---
title: "Ignoring Tax Interactions"
---

Ignoring the tax interaction between hedging instruments and the underlying portfolio is a common mistake. The three most material issues for US taxable investors are:

## Section 1256 Mark-to-Market

SPX and XSP index options are classified as Section 1256 contracts. This means:

- Positions are **marked to market at year-end** regardless of whether they have been sold
- Any unrealized gains or losses are recognized as of December 31
- All gains and losses receive **60/40 treatment** — 60% long-term capital gain, 40% short-term capital gain

This is generally favorable for a systematic put-buying program, as even short holding periods receive partial long-term capital gains treatment. However, it also means the tax cost of a hedge gain cannot be deferred beyond the tax year in which it accrues.

In practice, the automatic year-end loss recognition under Section 1256 provides a **tax benefit in most years** of a systematic put-buying program. Puts decay over time, producing unrealized losses that are recognized at year-end without requiring the position to be closed. This generates 60/40 capital losses that can offset gains elsewhere in the portfolio — automatically, without any selling. Unlike standard equity tax-loss harvesting, there is no need to sell and repurchase: the mark-to-market does it without disrupting the hedge. This reframes the Section 1256 mark-to-market from a neutral accounting rule to a modest tax efficiency that partially offsets the carry cost of the program in most years.

## Wash Sale Considerations When Rolling

The mistake here runs in both directions, and the second one is more common: assuming the wash sale rule constrains a roll schedule that it does not reach.

Section 1091 does not apply to Section 1256 contracts. Section 1256(f)(5) disapplies it to any loss taken into account under the mark-to-market rule described above [[26 U.S.C. § 1256]](../footnotes/index.md#irc-1256), and SPX puts, XSP puts, VIX options and options on index futures are all Section 1256 contracts — Section 1256(g)(6) confines "equity option" to options on stock and on narrow-based security indices, leaving broad-based index options outside it. This is the same provision that produces the automatic year-end loss recognition above: the losses are recognized by mark-to-market, and losses recognized that way are outside Section 1091 by statute. A roll schedule built on SPX or XSP does not need to avoid repurchasing within 30 days.

Section 1091 does apply to SPY puts and single-name equity puts, which sit outside Section 1256. If the program holds these as secondary instruments, rolling one at a loss into a substantially identical option within the 30-day window defers the loss, and the roll schedule for that sleeve needs to be checked against it [[26 U.S.C. §§ 1091 and 1092]](../footnotes/index.md#irc-1091-1092).

Section 1092, the straddle rules, is a separate provision and is not disapplied by Section 1256(f)(5). It asks whether a loss is offset by unrecognized gain on an offsetting position — a different question from whether a position was repurchased too soon. A hedge held against the portfolio it protects can raise mixed straddle questions regardless of its wash sale status. See [A3 Tax Considerations](../appendices/a3-tax-considerations-for-hedging-instruments.md) for the instrument-by-instrument treatment.

## Constructive Sale Rules for Collars

Under Section 1259, entering a collar — long put and short call on the same equity position — can be treated as a **constructive sale** if the collar eliminates substantially all risk of loss and opportunity for gain. This can:

- Trigger recognition of gain on the underlying equity position **without an actual sale**
- Affect the holding period of the underlying shares
- Create unexpected tax events for concentrated long-term appreciated positions

The key mitigant is to ensure the collar leaves meaningful upside exposure — a call strike at least 10–15% OTM typically avoids constructive sale treatment, but specific transactions should be reviewed by qualified tax counsel.

## Instrument Tax Comparison

| Instrument        | Tax Treatment                                     | Mark-to-Market at Year-End |
| ----------------- | ------------------------------------------------- | -------------------------- |
| SPX puts          | 60% LT / 40% ST (Section 1256)                    | Yes                        |
| XSP puts          | Same as SPX                                       | Yes                        |
| SPY puts          | Standard capital gains (holding period dependent) | No                         |
| VIX options       | Section 1256                                      | Yes                        |
| Single-stock puts | Standard capital gains                            | No                         |

See [A3 Tax Considerations](../appendices/a3-tax-considerations-for-hedging-instruments.md) for the full appendix treatment.

!!! warning "Not tax advice"

    All tax sections are for general orientation only. Specific treatment
    should be confirmed with qualified tax counsel before implementing any
    hedging strategy.
