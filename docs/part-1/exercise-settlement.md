---
title: "Exercise & Settlement"
---

## American Option

Can exercise anytime.

*Example:* Most US equity options.

## European Option

Exercise only at expiry.

*Example:* SPX index options.

## Assignment

Short option exercised against the investor.

*Example:* “Covered call got assigned.”

## Cash Settled

No shares exchanged — only cash difference.

*Example:* SPX options are cash settled.

## Settlement Mechanics

Cash settlement answers *what* changes hands. Two further questions decide what
the payment actually is: **when** the settlement value is struck, and **from
which prices**. Series listed on the same index answer them differently, and the
difference matters most in the situation a tail hedge exists for.

### AM and PM Settled Series

Standard monthly SPX options expire on the third Friday and are **AM-settled**:
the exercise-settlement value is calculated from the opening sales price, in its
primary market, of each component security of the index on the expiration date.
Trading in those series ordinarily ceases on the business day *before* — usually
the Thursday [[SPX Product Specifications]](../footnotes/index.md#cboe-spx-spec).

Cboe's SPXW series — the Weeklys and the end-of-month (EOM) contracts — are
**PM-settled**: the value is calculated from the last reported sales price of
each component on the expiration date itself, and trading in the expiring series
continues to the close that day. XSP is likewise PM-settled, against one-tenth
the official closing level of the index on the last trading day
[[XSP Product Specifications]](../footnotes/index.md#cboe-xsp-spec).

| Series                      | Settlement value struck from               | Last trading day                      |
| --------------------------- | ------------------------------------------ | ------------------------------------- |
| SPX standard (third Friday) | Component opening prices, expiration day   | Business day before, usually Thursday |
| SPXW Weeklys and EOM        | Component closing prices, expiration day   | Expiration day, at the close          |
| XSP                         | Official closing level of the index        | Expiration day, at the close          |

### SET and the Special Opening Quotation

The AM settlement value is a **Special Opening Quotation** (SOQ) of the index,
which Cboe publishes under the ticker **SET**. It is assembled from the opening
trade price of each component in its primary market; where a component does not
open that day, its last trade price from the prior session is used instead
[[SPX A.M. Settlement]](../footnotes/index.md#cboe-spx-am-settlement).

Three consequences follow, and none of them is intuitive:

- **SET is not the index's opening level.** The components do not all open
  simultaneously, so SET is assembled from prints struck at different moments.
- **SET is not anchored to a clock time.** There is no instant at which one can
  observe the settlement value forming.
- **SET is frequently a level the index never traded at.** On Cboe's own
  figures, the SOQ has landed *outside* the day's high-low range roughly 30% of
  the time, with a median deviation from the opening level of 0.09% and an
  extreme of 5.46% around March 2020.

### The Operator Principle

A general principle follows for any program holding AM-settled series:

!!! note

    Do not carry a position into AM settlement if the intention is to realise
    its value. Close or roll it while it is still tradable.

The reasoning is structural rather than a matter of taste. Between the Thursday
close and Friday's opening rotation, an AM-settled position **cannot be traded,
and its settlement value is not yet determined**. The holder is exposed to the
entire overnight move with no ability to act on it, and the level finally struck
need not be one at which the index traded at all. A position closed on the
Thursday realises an observable market price; a position held to settlement
accepts an unobservable one.

The exposure is symmetric — the gap can help as easily as it hurts — which is
precisely why it does not belong in a hedge program. A hedge is held to remove
uncertainty, and carrying it into settlement reintroduces a full session of
unmanaged index risk at the last moment. That objection applies with most force
when the position is deep in the money and being monetised under stress, since
the dollar value of a given percentage gap is then at its largest. See
[Crisis Execution Guidance](../part-8/crisis-execution-guidance.md).

PM-settled series do not raise the question: they trade until the close that
determines their settlement value.

### Exercise and Assignment Mechanics

SPX, SPXW and XSP are European, so no exercise notice can be submitted before
the expiration date and no early assignment is possible. Settlement is in cash,
delivered on the business day following expiration.

An in-the-money contract does not require its holder to do anything: the
clearing house exercises it automatically once it is in the money by more than a
small, exchange-defined threshold. The practical consequence is that a
long-dated hedge left unattended through expiration *will* settle, at whatever
value the applicable rule produces — an outcome that follows from inaction
rather than from a decision.

## LEAPS

Long-term equity anticipation securities (LEAPS) are options contracts with expiration dates extending beyond one year, often up to three years. These contracts allow investors to gain exposure to long-term price movements in the underlying asset, similar to standard options but with extended expiration periods [[Investopedia: LEAPS]](../footnotes/index.md#investopedia-leaps).
