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

### Cboe — VIX Historical Data { #cboe-vix-historical }

"Historical Price Data for VIX Index". Daily open/high/low/close for the VIX Index since 1990, published by Cboe as `VIX_History.csv` and updated daily. The High and Close columns are distinct figures and should not be conflated when citing a single-day peak.

[cboe.com — VIX Historical Data](https://www.cboe.com/en/tradable-products/vix/vix-historical-data/)

### Cboe — Put-Writing Strategy Research { #hist-put-writing }

Bondarenko, O. "Historical performance of put-writing strategies".

[cboe.com — Put-Write Research (PDF)](https://cdn.cboe.com/resources/education/research_publications/PutWriteCBOE19_v14_by_Prof_Oleg_Bondarenko_as_of_June_14.pdf)

### S&P Dow Jones Indices — S&P 500 { #spglobal }

"S&P 500® | S&P Dow Jones Indices".

[spglobal.com — S&P 500](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)

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
