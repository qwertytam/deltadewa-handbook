---
title: "A4 Crash Repricing Methodology"
---

Part VI defines crash convexity as $(V_{crash} - V_{today}) / Portfolio$ and stops
there. That is the right level for a definition and the wrong level for an
implementation: "hedge value after a simulated crash" does not say *which* legs
are valued, at what volatility, or whether the option still has time value left.
Two defects came out of that gap — one netting the equity loss into the
numerator, one valuing the crash leg at intrinsic — and between them they made a
correctly-sized book read as failing every scenario row. This appendix closes the
gap by stating exactly how $V_{crash}$ is formed.

It is a **description of the shipped engine**, written against
`deltadewa/analysis/crash_repricing.py` and `deltadewa/analysis/repricing.py`.
The normative specification, its acceptance tests, and the full derivation live in
[`docs/repricing-methodology.md`](https://github.com/qwertytam/deltadewa/blob/main/docs/repricing-methodology.md); where a number
appears in both, that document is the reference and this one is the summary.

## The three properties that pin $V_{crash}$

- **Hedge-only.** $V$ counts the **option legs only**. The underlying equity
  position is excluded from both terms. Convexity measures what the hedge does;
  netting the book's own loss into it answers a different question and always
  answers it badly.
- **Repriced, not intrinsic.** $V_{crash}$ is the legs **repriced** at the crash
  spot and crash volatility — full option value, time value included. Valuing
  them at intrinsic zeroes every strike more than the crash move out of the
  money, which is precisely the part of a tail ladder that is supposed to be
  working.
- **Instantaneous.** The crash is a jump **at the current valuation date**. Time
  to maturity does not change and the valuation date does not advance. A crash
  and a month of decay are separate questions and are kept separate.

## The crash state

From today's state — spot $S_0$, each leg's own $\sigma_i$, rate $r$, dividend
yield $q$, valuation date $t_0$ — the crash state is built as:

| Quantity             | Rule                                                                |
| -------------------- | ------------------------------------------------------------------- |
| Crash spot           | $S_{crash} = S_0 (1 + m)$, $m$ signed (e.g. $-0.25$)                |
| Crash vol, per leg   | $\sigma_{i,crash} = \sigma_{i} + \Delta\sigma + \kappa\, w_i$       |
| Rate, dividend yield | held at today's values                                              |
| Time to maturity     | unchanged                                                           |
| Engine               | European analytic Black–Scholes (QuantLib `AnalyticEuropeanEngine`) |

Rates typically fall in a crash and dividends are usually cut; both effects are
second-order for long puts against the spot and volatility moves, and both are
deliberately out of scope here.

## Skew treatment — why the vol shock is not flat

The first implementation bumped every leg by the same $\Delta\sigma$. That is
wrong in the direction that matters: in a real sell-off deep out-of-the-money
index puts gain **more** implied volatility than at-the-money ones — the put wing
steepens. In 2008 and 2020 the ≈10-delta wing ran 15+ volatility points over ATM
at the peak. A flat bump therefore understates the crash value of exactly the low
strikes a tail ladder is built from.

Each leg gets the flat bump plus a steepening term:

$$\sigma_{i,crash} = \sigma_i + \Delta\sigma + \kappa\, w_i,
\qquad
w_i = \begin{cases}
\min\!\left(1,\; \dfrac{\ln(S_0/K_i)}{\ln(S_0/K_{ref,i})}\right) & K_i < S_0 \text{ (OTM put)}\\[1.2em]
0 & \text{calls, ATM/ITM puts}
\end{cases}$$

Three properties of that expression carry the weight:

**The anchor is per-leg.** $K_{ref,i}$ is *leg $i$'s own* ≈10-delta wing — the
strike whose European put-delta magnitude equals the configured reference delta,
solved at **that leg's own tenor and today-volatility**. It is a property of the
strike and the tenor, not of the book. An earlier version anchored the steepening
to the deepest put the book actually held, which meant a leg's crash volatility
moved when an unrelated leg was added or removed, and meant a standalone
candidate priced on a different basis than the same strike held in the book. With
the per-leg anchor, a candidate priced at a held strike reproduces that held leg's
per-contract crash value exactly.

**The weight is linear in log-moneyness**, zero at the money and rising to one at
the leg's own wing. Calls and at- or in-the-money puts do not steepen.

**The steepening is capped at the wing, never extrapolated.** For a put deeper
than its own ≈10-delta wing the $\min$ binds and the add-on holds flat at
$\kappa$. This is deliberate: $\kappa$ is calibrated to the ≈10-delta wing, and no
skew observation constrains the model past it. Extrapolating the slope into the
5- or 2-delta region would invent implied volatility the historical episodes do
not pin down. Holding it flat under-states deep-tail IV, and therefore
under-states protection — the safe direction of error for a tail program.

Setting $\kappa = 0$ recovers the flat bump exactly and solves no wing at all, so
the knob can be turned off without changing any other number.

## Formula

$$V_{today} = \sum_i \text{price}\big(S_0,\,K_i,\,\sigma_i,\,r,\,q,\,T_i\big)\cdot q_i \cdot c_i$$

$$V_{crash} = \sum_i \text{price}\big(S_{crash},\,K_i,\,\sigma_i + \Delta\sigma + \kappa\,w_i,\,r,\,q,\,T_i\big)\cdot q_i \cdot c_i$$

with $q_i$ the signed contract quantity, $c_i$ the contract size, and $T_i$
unchanged. The denominator is the protected book — the equity notional today —
so the numerator is a change in *hedge* value and the denominator is a *book*
value.

An **intrinsic floor** is also computed, as a conservative lower bound:

$$V_{crash}^{floor} = \sum_i \max\big(K_i - S_{crash},\,0\big)\cdot q_i \cdot c_i \quad \text{(puts)}$$

It is a labelled secondary figure and must never be the headline. The worked
example below shows why: it reads 2.5× where the repriced value reads 17.5×.

## Worked example

A \$20M book hedged with a three-rung ladder at 20/30/40% out of the money,
18-month tenor, 23/26/16 contracts, European puts. Spot 6600, today-volatility
20% flat, $r = 4.5\%$, $q = 1.5\%$, contract size 100. Crash move $-25\%$
($S_{crash} = 4950$), flat bump $\Delta\sigma = +0.15$, steepening
$\kappa = +0.10$ anchored at the 0.10 put-delta wing.

At this common tenor and today-volatility all three rungs share a wing at
$K_{ref} \approx 5213$ — about 21% out of the money. The 20% rung sits just
*shallower* than its wing and so reaches $w = 0.95$; the 30% and 40% rungs sit
*past* it and cap at the full $\kappa$:

| Leg       | Strike | Qty | $w$  | Crash vol | Value today   | Value in crash  |
| --------- | ------ | --- | ---- | --------- | ------------- | --------------- |
| 20% OTM   | 5280   | 23  | 0.95 | 44.5%     | \$219,392     | \$2,524,349     |
| 30% OTM   | 4620   | 26  | 1.00 | 45.0%     | \$70,696      | \$1,961,615     |
| 40% OTM   | 3960   | 16  | 1.00 | 45.0%     | \$7,627       | \$740,040       |
| **Hedge** |        |     |      |           | **\$298,099** | **\$5,226,004** |

- Hedge value today ≈ **\$298,099** — about 1.49% of the book, roughly 1%/yr of
  carry. The skew is a crash-state effect, so this figure is unchanged by it.
- Hedge value in the crash **\$5,226,004** — a **≈17.5×** multiple.
- Intrinsic floor **\$759,000** — only **2.5×**, and it zeroes the 30% and 40%
  rungs entirely.

$$\text{convexity} = \frac{5{,}226{,}004 - 298{,}099}{20{,}000{,}000} = \mathbf{+24.6\%}$$

For contrast, the same book on the **flat** bump — every leg at 35% crash vol —
reprices to \$3,897,393, a 13.1× multiple and **+18.0%** convexity. The
difference is entirely the two deep rungs, and it is convexity the flat bump was
understating rather than convexity the skew invents. The intrinsic basis, for its
part, gives $(759{,}000 - 298{,}099)/20{,}000{,}000 = +2.3\%$ — which, with the
equity loss netted in on top, is how a conformant book once read as failing.

These are the engine's own outputs, pinned as regression goldens in
`tests/test_analysis/test_crash_repricing.py`. They agree with the closed-form
Black–Scholes table in the normative document to within its stated ~0.5%
tolerance; the residual is day-count and calendar convention, not a
disagreement.

## Reproducibility — how the basis reaches the pricer

The methodology above is only reproducible if every surface prices against the
same basis. Two structural decisions in the implementation are what make that
true, and both exist because the alternative failed in practice.

**The basis travels as one value object.** The four *pricing* inputs — crash
depth, flat volatility bump, steepening, and the reference delta the steepening
is anchored to — are bundled into a single frozen `CrashShock`, built from policy
in one place. Before that they were threaded as individual scalars, and the
reference delta was quietly dropped en route to the book gauges, which then
priced against the pricing primitive's own internal default. The result was
invisible at the shipped default and divergent the moment the anchor was tuned:
the sizing workbench honoured it and the gauges did not. Bundling makes a
partially-stated crash basis unrepresentable.

**No crash-pricing input carries a default, anywhere.** Every entry point that
reprices at the crash state takes a `CrashShock`, required, with no default value
— so a surface cannot state part of the basis and silently inherit the rest, and
cannot reprice spot-only by omission. This is enforced structurally rather than
by convention: a test walks the package's syntax tree and fails if any
crash-pricing parameter acquires a default. Sweeping surfaces (shock grids,
payoff ladders, summary rungs) change *depth* through a method that carries the
volatility basis along by construction, so walking a grid cannot drop the skew.

The IPS **target band** deliberately does *not* travel on this object. Pricing
and policy stay separable, so omitting the band fails the band comparison
outright rather than quietly changing what was priced.

One consequence worth stating plainly: because the mapping is per-leg and the
anchor is absolute, the crash number is the same across every surface at equal
depth — gauge, scenario table, payoff ladder, sizing workbench, strike ladder,
roll trigger. Disagreement between two panels is a bug, not a modelling choice.

## Policy keys

All of these live in the `convexity:` section of `config/ips.yaml`. They are
policy, not presentation, and belong in the IPS rather than in dashboard config.

| Key                    | Meaning                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `crash_scenario_pct`   | Signed crash move as a **percent** (e.g. `-25.0`). Required — the single source of the crash depth for every panel.                |
| `crash_vol_shock`      | Flat additive volatility bump as a decimal (e.g. `0.15`).                                                                          |
| `skew_steepening`      | Extra volatility reached at each leg's own wing, on top of the flat bump. `0.0` recovers the flat bump.                            |
| `skew_reference_delta` | Put-delta magnitude of the wing the steepening is anchored to (e.g. `0.10`). Only consulted when `skew_steepening` is non-zero.    |
| `crash_floor_reported` | Whether to surface the intrinsic-floor column. Presentation of a computed figure, not a pricing input — it stays off `CrashShock`. |

> **The floor is an opt-out.** `crash_floor_reported: false` removes the
> per-contract intrinsic floor from `/design`'s sizing panel — the only live
> surface that reports it — leaving every other figure unchanged. The default
> is `true`. A program may reasonably decline it: the floor reads far below the
> repriced payoff (2.5× against 17.5× in the worked example above), so a reader
> who mistakes it for the headline understates the protection on offer. The key
> was inert until #273 wired it to that panel; before then its only reader was
> the retired Jupyter display layer.

**Calibrating the volatility inputs.** In 2008 and 2020 index-put implied
volatilities expanded roughly +20 to +40 points at the peak; `+0.15` is a
deliberately conservative mid-cycle ATM baseline. For the steepening, the
≈10-delta wing ran 15+ points over ATM in those same episodes; `+0.10` is a
conservative central estimate with a plausible range of +0.05 to +0.20. Both are
derived from the historical episodes alone and **never tuned to make a book's
convexity land inside its target band** — a shock calibrated to the answer you
want measures nothing. Understating either errs toward less apparent protection,
which is the correct direction to be wrong in.

## What this model does not do

- **No term structure of skew.** The steepening is one cross-sectional slope. Each
  leg's *own* tenor is already captured, since its wing is solved at that tenor
  and today-volatility; what is not modelled is how the slope itself varies
  across tenors. That is the natural next refinement.
- **Rates and dividends held constant**, as noted above.
- **A single instantaneous jump.** The path a crash takes — and the interaction
  between decay and the crash arriving later — is not modelled here. That is the
  Monte Carlo surface's question, not this one.
- **The crash volatility is assumed, not observed.** Nothing in this repricing
  reads a live volatility surface; $\Delta\sigma$ and $\kappa$ are policy
  parameters expressing a view about crash conditions. The output is only as good
  as that view, and it should be revisited when the view changes.
