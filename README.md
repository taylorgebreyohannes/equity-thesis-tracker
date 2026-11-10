# equity-thesis-tracker

A reproducible Python, SQL, pandas and NumPy project that turns a finished Citadel stock pitch memo on **GE Vernova (NYSE: GEV)** into a testable, trackable investment thesis and checks whether it held up after Q3 earnings on 2026-10-28.

## Thesis snapshot

| Item | Value |
|------|-------|
| Ticker | GEV (NYSE) |
| Rating | SHORT |
| Price at pitch (2026-10-01) | $987.45 |
| Price target | $746 |
| Bear / Base / Bull | $441 / $668 / $1,207 |
| Scenario probabilities | 25% / 50% / 25% |

The target is the probability-weighted value: 0.25 x 441 + 0.50 x 668 + 0.25 x 1207 = 746, verified exactly in `tests/test_thesis.py`.

## Research question

Did the market's reaction to the 2026-10-28 Q3 earnings, relative to peers, move toward the bear, base or bull scenario?

## Roadmap

- [x] 1. Repo and README skeleton
- [ ] 2. SQL database: prices, peer multiples, financials (GEV, Eaton, Siemens Energy)
- [ ] 3. Valuation module with tests reproducing the $746 target
- [ ] 4. Metrics and event-study notebook around 2026-10-28
- [ ] 5. Results memo with charts
- [ ] 6. Polished final repo

Details and quantitative stretch goals for each step are in [docs/ROADMAP.md](docs/ROADMAP.md).

## Repo layout

```
config/       thesis inputs (single source of truth)
src/          equity_thesis_tracker package (valuation, metrics, db helpers)
sql/          schema and queries (deliverable 2)
notebooks/    event study (deliverable 4)
reports/      results memo and figures (deliverable 5)
data/         raw and processed data (gitignored, rebuilt by scripts)
tests/        pytest suite
```

## Quickstart

```bash
git clone <your-repo-url> && cd equity-thesis-tracker
python -m venv .venv && source .venv/bin/activate
make install
make test
make summary
```

## Methodology

_To be filled in as deliverables 3 and 4 are completed: valuation approach, event-study design, data sources and dates._

## Results

_To be filled in at deliverable 5._

## Limitations

_To be filled in at deliverable 5._

## Disclaimer

Educational project. Nothing here is investment advice.
