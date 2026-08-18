---
title: "References"
---

Sources cited throughout the handbook, grouped by type. Each entry is linked
from the pages that cite it — use your browser's back button to return to where
you were reading.

## Books and Practitioner Texts

### Bhansali (2014) — Tail Risk Hedging { #bhansali }

Bhansali, V. (2014) *Tail Risk Hedging: Creating Robust Portfolios for Volatile
Markets*.

The most complete published framework for quantifying hedge payoff ratios and
scenario-based tail protection. Bhansali was Head of Portfolio Management at
PIMCO, and this book is the closest thing to an institutional standard for the
methodology behind these metrics.

### Bennett (2014) — Trading Volatility { #bennett }

Bennett, C. (2014) *Trading Volatility, Correlation, Term Structure and Skew*.

The chapter on term structure and carry is the most thorough practitioner
treatment of this topic, and directly addresses how roll yield affects
long-dated option positions. Available freely at trading-volatility.com.

### Sinclair (2013) — Volatility Trading { #sinclair }

Sinclair, E. (2013) *Volatility Trading*, 2nd ed.

Chapter 4 and related sections on carry and the volatility risk premium provide
a quantitative treatment of how the term structure slope affects rolling
strategies.

## Institutional and Practitioner Research

### Meketa (2019) — Tail Risk Hedging { #meketa }

Meketa Investment Group. (2019) "Tail Risk Hedging". Available publicly at
meketa.com.

Uses loss-offset framing explicitly, and provides historical context for what
offset ratios are achievable at different carry budgets.

### Cambridge Associates (2025) — Portfolio Protection { #cambridge }

Cambridge Associates. (2025) "Portfolio Protection: Challenges with Equity Put
Options".

Uses similar scenario payoff framing, and is directly addressed at institutional
investors and family offices evaluating derivatives-based protection.

### CAIA (2021) — Tail Risk Hedging { #caia }

Levine, A., Ooi, Y. (2021) "Tail Risk Hedging". Available at caia.org.

Discusses the cost-per-payoff framing in a format accessible to allocators.

### Gateway / GIA — Customizable Tail Risk Hedging { #gateway }

"Convexity: A Powerful and Customizable Approach to Tail Risk Hedging".

[gia.com — Convexity: A Powerful and Customizable Approach to Tail Risk Hedging (PDF)](https://www.gia.com/wp-content/uploads/2022/03/Convexity-A-Powerful-and-Customizable-Approach-to-Tail-Risk-Hedging.pdf)

### Resonanz Capital — Strategic Tail-Risk Hedging { #resonanzcapital }

"Strategic Tail-Risk Hedging: Building Antifragility into Institutional
Portfolios".

[resonanzcapital.com — Strategic Tail-Risk Hedging](https://resonanzcapital.com/insights/strategic-tail-risk-hedging-building-antifragility-into-institutional-portfolios)

### Informa Connect — Convexity versus Skewness { #informaconnect }

"Assessing the risk-profile of quant strategies: convexity vs skewness".

[informaconnect.com — Assessing risk-profile of quant strategies](https://informaconnect.com/assessing-risk-profile-of-quant-strategies-the-convexity-vs-skewness/)

### Alpha Architect — Strategies to Mitigate Tail Risk { #alpha-arch }

"Strategies to Mitigate Tail Risk".

[alphaarchitect.com — Strategies to Mitigate Tail Risk](https://alphaarchitect.com/strategies-to-mitigate-tail-risk/)

### Mutiny Fund — Tail Hedging Books { #mutinyfund }

"The Best Tail Hedging Books for Beginners".

[mutinyfund.com — Best Tail Hedging Books](https://mutinyfund.com/best-tail-hedging-books/)

## Exchange and Index Methodology

### Cboe — SPX Index Options Product Specifications { #cboe-spx-spec }

Cboe Exchange, Inc. "SPX Index Options" (summary product specifications fact
sheet).

[cdn.cboe.com — SPX Index Options Fact Sheet (PDF)](https://cdn.cboe.com/resources/spx/spx-fact-sheet.pdf)

Cboe's own contract specification for SPX and SPXW: European exercise, cash
settlement, the AM (opening-price) versus PM (closing-price) calculation of the
exercise-settlement value, the rule that trading in standard series ceases the
business day before expiration, and cash delivery on the following business day.
Its comparison table also classifies SPY options as American-style, physically
settled and PM-settled at expiration.

### Cboe — Settlement of Standard, AM-Settled S&P 500 Index Options { #cboe-spx-am-settlement }

Cboe Exchange, Inc. "Settlement of Standard, A.M.-Settled S&P 500 Index
Options", version 2, 17 July 2024.

[cdn.cboe.com — Settlement of Standard AM-Settled SPX Options (PDF)](https://cdn.cboe.com/resources/spx/Settlement_of_Standard_AM_Settled_SP_500_Index_Options.pdf)

Cboe's explanation of the Special Opening Quotation: that the AM settlement
value is published under the ticker SET, how it is assembled from component
opening trade prices, the fallback to the prior session's last trade for a
component that does not open, and the historical dispersion of the SOQ against
the opening level and the day's traded range.

### Cboe — XSP (Mini-SPX) Index Options Product Specifications { #cboe-xsp-spec }

Cboe Exchange, Inc. "XSP Index Options" (summary product specifications fact
sheet).

[cdn.cboe.com — XSP Index Options Fact Sheet (PDF)](https://cdn.cboe.com/resources/xsp/XSP_Options_Fact_Sheet.pdf)

Cboe's own contract specification for Mini-SPX: European exercise, cash
settlement, PM settlement against one-tenth the official closing level of the
index on the last trading day, and third-Friday standard expirations alongside
Weeklys and end-of-month series.

### Cboe — Why Option Settlement Style Matters { #cboe-settlement-style }

Cboe Exchange, Inc. "Why Option Settlement Style Matters".

[cboe.com — Why Option Settlement Style Matters](https://www.cboe.com/insights/posts/why-option-settlement-style-matters)

Cboe's statement that equity and ETF options, SPY among them, deliver shares
physically when exercised or assigned, in contrast to the cash settlement of SPX
and XSP.

### Cboe — VIX Term Structure { #cboe-vix-term-structures }

*Note:* While focused on VIX futures, the Cboe's published term structure data
and methodology documentation provides the cleanest public illustration of how
the contango/backwardation distinction generates roll costs and benefits over
time.

[cboe.com — VIX Term Structure](https://www.cboe.com/tradable-products/vix/term-structure)

### Cboe — VIX Mathematics Methodology { #cboe-vix-maths }

"Cboe Volatility Index Mathematics Methodology".

[cboe.com — VIX Mathematics Methodology (PDF)](https://cdn.cboe.com/resources/indices/Cboe_Volatility_Index_Mathematics_Methodology.pdf)

### Cboe — S&P 500 Put Protection Indices { #cobe-pp-indices }

"Cboe S&P 500 Put Protection Indices Methodology".

[cboe.com — Put Protection Indices Methodology (PDF)](https://cdn.cboe.com/api/global/us_indices/governance/Cboe_SP_500_Put_Protection_Indices_Methodology.pdf)

### Cboe — SKEW Index Methodology { #cboe-skew-methodology }

Cboe Exchange, Inc. "The Cboe Skew Index — SKEW", white paper, January 2011.

[cdn.cboe.com — The Cboe Skew Index White Paper (PDF)](https://cdn.cboe.com/resources/indices/documents/SKEWwhitepaperjan2011.pdf)

Cboe's own derivation of SKEW: a risk-neutral estimate of the 30-day S&P 500
log-return skewness coefficient, computed from a strip of out-of-the-money SPX
options by the same replication technique as VIX, and transformed so that 100
represents a normal distribution and higher readings mean more negative tail
skew. This is the authority for describing SKEW as a moment-based index rather
than a two-strike volatility spread.

!!! warning

    Cboe opened a consultation in May 2025 proposing to replace this
    methodology with a differential or ratio of 25-delta put and call strikes.
    The July 2025 consultation results record that the Index Committee
    determined modifications are appropriate, but state that an effective date
    "will be announced when it is available" — no replacement formula had been
    published at the time of citation. Verify against Cboe's live methodology
    before relying on this document for the formula in force on a given date.

### Cboe — SKEW Historical Data { #cboe-skew-historical }

Cboe Exchange, Inc. "Historical Price Data for the Cboe SKEW Index". Daily
closing values published as `SKEW_History.csv`.

[cdn.cboe.com — SKEW Historical Data (CSV)](https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv)

The primary source for the length of the available SKEW history and for any
claim about the index's historical range. The daily series begins 2 January
1990, which is what makes lookback windows longer than a few years possible at
all.

### Cboe — VIX Historical Data { #cboe-vix-historical }

"Historical Price Data for VIX Index". Daily open/high/low/close for the VIX Index since 1990, published by Cboe as `VIX_History.csv` and updated daily. The High and Close columns are distinct figures and should not be conflated when citing a single-day peak.

[cboe.com — VIX Historical Data](https://www.cboe.com/en/tradable-products/vix/vix-historical-data/)

### Cboe — Put-Writing Strategy Research { #hist-put-writing }

Bondarenko, O. "Historical performance of put-writing strategies".

[cboe.com — Put-Write Research (PDF)](https://cdn.cboe.com/resources/education/research_publications/PutWriteCBOE19_v14_by_Prof_Oleg_Bondarenko_as_of_June_14.pdf)

### S&P Dow Jones Indices — S&P 500 { #spglobal }

"S&P 500® | S&P Dow Jones Indices".

[spglobal.com — S&P 500](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)

## Regulatory and Legal Sources

### Federal Reserve Board — Regulation T, Options Margin { #cfr-220-12-options }

12 CFR 220.12(f)(1), "Supplement: margin requirements" (Regulation T, Credit by
Brokers and Dealers).

[govinfo.gov — 12 CFR Part 220 (Regulation T)](https://www.govinfo.gov/content/pkg/CFR-2023-title12-vol3/xml/CFR-2023-title12-vol3-part220.xml)

Establishes that for exchange-listed options the margin amount is the one
specified by the rules of the registered exchange or securities association on
which the option trades, subject to SEC approval. This is the authority for
describing listed-option margin as set by exchange and SRO rules rather than by a
Regulation T percentage.

### FINRA — Rule 4210, Margin Requirements { #finra-4210 }

FINRA Rule 4210, "Margin Requirements", including 4210(f)(2)(E) on uncovered
short index options and 4210(f)(2)(H) on spreads.

[finra.org — 4210. Margin Requirements](https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210)

The strategy-based margin rule for FINRA member firms. Sets the premium-plus-
percentage formula for uncovered short broad-based index options — 15% of the
underlying index value less the out-of-the-money amount, floored at 10% — and the
treatment of spreads, where the long leg is paid for in full and the short leg is
margined at the lesser of the uncovered requirement or the maximum potential
loss.

### FINRA — Interpretations of Rule 4210, Portfolio Margin { #finra-4210-interps }

FINRA, "Interpretations of Rule 4210", portfolio margin sections under 4210(g).

[finra.org — Interpretations of Rule 4210](https://www.finra.org/rules-guidance/guidance/interps-4210)

States the theoretical-pricing-model stress ranges used to compute portfolio
margin — −8% to +6% for a high-capitalisation broad-based index and −10% to +10%
for a non-high-capitalisation broad-based index — and the minimum account equity
tiers, which depend on whether the firm has full real-time intraday monitoring
capability.

### Cboe — Complex Orders (Rules 1.1 and 5.33) { #cboe-complex-orders }

Cboe Exchange, Inc. *Rules of Cboe Exchange, Inc.*, Rule 1.1 (definition of
"complex order") and Rule 5.33 (complex orders).

[cboe.com — Rules of Cboe Exchange, Inc. (PDF)](https://cdn.cboe.com/resources/regulation/rule_book/C1_Exchange_Rule_Book.pdf)

Defines a complex order as the concurrent execution of two or more series in the
same underlying security or index, for the same account, to accomplish a
particular strategy, and governs execution of such orders as a single net-priced
package rather than as separately worked legs.

## Data Sources

### FRED — Treasury Constant Maturity Yields { #fred }

Board of Governors of the Federal Reserve System (US). "Market Yield on U.S.
Treasury Securities at Constant Maturity" (DGS series). Retrieved from FRED,
Federal Reserve Bank of St. Louis.

[fred.stlouisfed.org — DGS10](https://fred.stlouisfed.org/series/DGS10)

## Academic and General Reference

### Artzner et al. (1999) — Coherent Measures of Risk { #artzner }

Artzner, P., Delbaen, F., Eber, J.-M., Heath, D. (1999) "Coherent Measures of
Risk", *Mathematical Finance*, 9(3), pp. 203–228.

The academic foundation for preferring CVaR / Expected Shortfall over VaR.

### Wikipedia — Greeks (finance) { #wiki-greeks }

[en.wikipedia.org — Greeks (finance)](https://en.wikipedia.org/wiki/Greeks_%28finance%29)

### Investopedia — LEAPS { #investopedia-leaps }

"LEAPS: How Long-Term Equity Anticipation Securities Options Work".

[investopedia.com — LEAPS](https://www.investopedia.com/terms/l/leaps.asp)
