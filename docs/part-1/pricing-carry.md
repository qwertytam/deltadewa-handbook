---
title: "Pricing & Carry"
---

#### Spot Price (\$S$)

Current underlying price.

*Example:* “Model uses spot = 5235.”

#### Forward Price (\$F$)

Future implied price including carry.

*Example:* “SPX forwards embed rates minus dividends.”

#### Risk-Free Rate (\$r$)

Discounting rate used in pricing.

*Example:* “Long-dated calls are sensitive to rates.”

#### Dividend Yield (\$q$)

Expected dividends (or index carry).

*Example:* “Higher dividends lower call value.”

Note: When using SPX puts to hedge a portfolio whose dividend yield differs materially from the S&P 500's dividend yield, a carry differential arises. The SPX option is priced off the index forward (which embeds the index dividend yield), but the portfolio being hedged pays a different yield. For a portfolio with a significantly higher dividend yield than the SPX, the index put is slightly underpriced relative to the portfolio's own put-equivalent; for a lower-yield portfolio, the reverse. This is typically a second-order effect for diversified large-cap portfolios, but can be meaningful for portfolios with a strong income or low-dividend tilt relative to the index.

#### Implied Volatility (IV)

Volatility implied by market price.

*Example:* “IV below the 20th historical percentile is generally considered cheap.”

#### Realized (Historical) Volatility

Actual past price movement.

*Example:* “Realized volatility came in below implied volatility.”

