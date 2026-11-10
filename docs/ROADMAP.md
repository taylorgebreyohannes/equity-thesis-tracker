# Roadmap: six deliverables, each with a quant stretch

| # | Deliverable | Core | Quant / technical stretch (where the learning is) |
|---|-------------|------|----------------------------------------------------|
| 1 | Repo + README skeleton | Package layout, config, tests, CI | Decimal-exact arithmetic, typed frozen dataclasses, TDD on the $746 identity, GitHub Actions |
| 2 | SQL database | Prices, peer multiples, financials for GEV, Eaton, Siemens Energy in SQLite | Normalized schema with keys and constraints, window functions (rolling returns, peer percentile ranks), as-of joins for point-in-time fundamentals, FX normalization for Siemens Energy (EUR), data-quality checks |
| 3 | Valuation module + tests | Reproduce the $746 target | Property-based tests (hypothesis), Monte Carlo over scenario distributions, sensitivity grids, reverse DCF (what growth the $987.45 price implies), implied scenario probabilities |
| 4 | Metrics + event-study notebook | Returns around 2026-10-28 | Market-model (CAPM) estimation window, abnormal and cumulative abnormal returns, t-statistics, bootstrap confidence intervals, placebo-date test, peer-adjusted returns, volatility regimes (EWMA/GARCH) |
| 5 | Results memo + charts | Did the thesis hold up? | Scenario calibration scoring (Brier score), realized vs. bear/base/bull paths, short P&L attribution (price, borrow cost, dividends), Kelly-style sizing sensitivity |
| 6 | Polished repo | Resume-ready | CI badge, pinned environment, one-command reproduce (`make all`), results table auto-generated into README, tagged release v1.0 |

## Build order rule

Every stretch item gets a test or a notebook cell that proves it works before it earns a README claim.
