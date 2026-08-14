---
title: "Basis Risk"
---

Basis risk is the risk that the hedge does not move in lockstep with the actual portfolio during a market decline. For SPX put options, basis risk arises from the mismatch between the S&P 500 index and the investor's specific holdings.

#### Sources of Basis Risk

| Source                 | Description                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| Sector concentration   | A portfolio heavy in technology or energy may diverge from broad SPX during a sector-specific sell-off |
| Single-stock exposure  | Concentrated positions in individual names are not hedged by an index put                              |
| International holdings | Non-US equities may correlate differently with SPX across regimes                                      |
| Small-cap tilt         | Small-cap portfolios typically fall further than large-cap in crises and may recover differently       |

#### When Basis Risk Is Low

Basis risk is low when the portfolio closely tracks the S&P 500. For a diversified large-cap US equity portfolio with a beta near 1.0, SPX puts typically provide effective systemic protection.

#### When Basis Risk Is High

For concentrated or sector-heavy portfolios, SPX puts may provide poor hedge efficiency in some scenarios. If the portfolio is primarily technology stocks and a sell-off is tech-specific rather than broad-market, the SPX put will underperform relative to what the portfolio actually needs.

Mitigation options:

1. **Accept the basis risk** — recognize that the hedge covers systemic market declines but not idiosyncratic single-stock or sector drawdowns. This is the correct choice for most diversified family office portfolios.
2. **Sector ETF options** — use sector-specific puts (e.g., QQQ puts for a technology-heavy portfolio) alongside SPX puts.
3. **Single-name options** — buy puts on concentrated individual positions. More expensive but eliminates basis risk for those names.
4. **Hybrid approach** — use SPX puts for broad market risk and single-name puts for any position above a concentration threshold (e.g., greater than 5% of portfolio).

The correct approach depends on portfolio composition and available budget. For highly concentrated portfolios, the basis mismatch should be explicitly acknowledged in the IPS.

#### Correlation Regime Shifts Within the Portfolio

A related but distinct source of basis risk is the breakdown of within-portfolio correlations during non-systemic drawdowns. The standard tail-hedging assumption is that in a severe crash, equity correlations converge toward 1.0 — all positions fall together, and the SPX put hedges the aggregate loss effectively. This holds in systemic crises (2008, 2020).

However, in factor-driven or sector-specific drawdowns, correlations can diverge sharply. In 2022, for example, the S&P 500 fell approximately 25%, but within the index, energy stocks gained roughly 60% while technology stocks fell roughly 33%. A portfolio concentrated in technology experienced a drawdown materially worse than 25%, while an SPX put was sized and calibrated to the broad index decline.

This means basis risk is not solely a function of portfolio beta — it also depends on which sectors or factors drive any given drawdown. Investors with significant sector tilts should recognize that their realized hedge effectiveness in a factor-driven sell-off may be lower than scenario analysis against broad SPX suggests.

