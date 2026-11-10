from dataclasses import replace
from decimal import Decimal

import pytest

from equity_thesis_tracker import Scenario, Thesis, load_thesis


def test_probabilities_sum_to_one():
    t = load_thesis()
    assert sum(s.probability for s in t.scenarios) == Decimal(1)


def test_expected_value_reproduces_memo_target_exactly():
    t = load_thesis()
    assert t.expected_value() == Decimal(746)
    assert t.expected_value() == t.price_target


def test_short_thesis_implies_price_decline_and_positive_position_return():
    t = load_thesis()
    assert t.implied_return() < 0
    assert t.position_return() == -t.implied_return()
    assert t.position_return() > 0


def test_scenario_returns_ordered_bear_to_bull():
    r = load_thesis().scenario_returns()
    assert r["bear"] < r["base"] < r["bull"]


def test_bad_probabilities_rejected():
    t = load_thesis()
    bad = tuple(replace(s, probability=Decimal("0.30")) for s in t.scenarios)
    with pytest.raises(ValueError, match="sum to 1"):
        Thesis(t.ticker, t.rating, t.price_date, t.price, t.price_target, bad)


def test_bad_rating_rejected():
    t = load_thesis()
    with pytest.raises(ValueError, match="rating"):
        Thesis(t.ticker, "HOLD", t.price_date, t.price, t.price_target, t.scenarios)


def test_scenario_is_immutable():
    s = Scenario("x", Decimal(1), Decimal(1))
    with pytest.raises(AttributeError):
        s.price = Decimal(2)  # type: ignore[misc]
