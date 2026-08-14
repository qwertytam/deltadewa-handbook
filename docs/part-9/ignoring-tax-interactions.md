---
title: "Ignoring Tax Interactions"
---

Ignoring the tax interaction between hedging instruments and the underlying portfolio is a common mistake. The three most material issues for US taxable investors are:

#### Section 1256 Mark-to-Market

SPX and XSP index options are classified as Section 1256 contracts. This means:

- Positions are **marked to market at year-end** regardless of whether they have been sold
- Any unrealized gains or losses are recognized as of December 31
- All gains and losses receive **60/40 treatment** — 60% long-term capital gain, 40% short-term capital gain

This is generally favorable for a systematic put-buying program, as even short holding periods receive partial long-term capital gains treatment. However, it also means the tax cost of a hedge gain cannot be deferred beyond the tax year in which it accrues.

In practice, the automatic year-end loss recognition under Section 1256 provides a **tax benefit in most years** of a systematic put-buying program. Puts decay over time, producing unrealized losses that are recognized at year-end without requiring the position to be closed. This generates 60/40 capital losses that can offset gains elsewhere in the portfolio — automatically, without any selling. Unlike standard equity tax-loss harvesting, there is no need to sell and repurchase: the mark-to-market does it without disrupting the hedge. This reframes the Section 1256 mark-to-market from a neutral accounting rule to a modest tax efficiency that partially offsets the carry cost of the program in most years.

#### Wash Sale Considerations When Rolling

When rolling options at a loss, the wash sale rule can potentially apply if a substantially identical position is repurchased within 30 days before or after the sale. For broad index options, this is less commonly an issue than for single-name options, but the interaction between rolling losses and wash sale rules should be reviewed with tax counsel when designing a systematic roll program.

#### Constructive Sale Rules for Collars

Under Section 1259, entering a collar — long put and short call on the same equity position — can be treated as a **constructive sale** if the collar eliminates substantially all risk of loss and opportunity for gain. This can:

- Trigger recognition of gain on the underlying equity position **without an actual sale**
- Affect the holding period of the underlying shares
- Create unexpected tax events for concentrated long-term appreciated positions

The key mitigant is to ensure the collar leaves meaningful upside exposure — a call strike at least 10–15% OTM typically avoids constructive sale treatment, but specific transactions should be reviewed by qualified tax counsel.

#### Instrument Tax Comparison

| Instrument        | Tax Treatment                                     | Mark-to-Market at Year-End |
| ----------------- | ------------------------------------------------- | -------------------------- |
| SPX puts          | 60% LT / 40% ST (Section 1256)                    | Yes                        |
| XSP puts          | Same as SPX                                       | Yes                        |
| SPY puts          | Standard capital gains (holding period dependent) | No                         |
| VIX options       | Section 1256                                      | Yes                        |
| Single-stock puts | Standard capital gains                            | No                         |

See See A3 Tax Considerations for the full appendix treatment.

