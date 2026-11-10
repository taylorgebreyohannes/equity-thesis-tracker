"""Thesis inputs and the probability-weighted price target.

Decimal is used everywhere so the memo's numbers reproduce exactly, with no rounding.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config" / "thesis.toml"


@dataclass(frozen=True)
class Scenario:
    name: str
    price: Decimal
    probability: Decimal


@dataclass(frozen=True)
class Thesis:
    ticker: str
    rating: str
    price_date: str
    price: Decimal
    price_target: Decimal
    scenarios: tuple[Scenario, ...]

    def __post_init__(self) -> None:
        total = sum((s.probability for s in self.scenarios), Decimal(0))
        if total != Decimal(1):
            raise ValueError(f"scenario probabilities must sum to 1, got {total}")
        if self.rating not in {"LONG", "SHORT"}:
            raise ValueError(f"rating must be LONG or SHORT, got {self.rating!r}")

    def expected_value(self) -> Decimal:
        """Probability-weighted price: E[P] = sum(p_i * P_i)."""
        return sum((s.probability * s.price for s in self.scenarios), Decimal(0))

    def implied_return(self) -> Decimal:
        """Price return to the target from the pitch price: target / price - 1."""
        return self.price_target / self.price - Decimal(1)

    def position_return(self) -> Decimal:
        """Return to the position: sign-flipped for a SHORT."""
        r = self.implied_return()
        return -r if self.rating == "SHORT" else r

    def scenario_returns(self) -> dict[str, Decimal]:
        """Price return of each scenario from the pitch price."""
        return {s.name: s.price / self.price - Decimal(1) for s in self.scenarios}


def load_thesis(path: Path | str = DEFAULT_CONFIG) -> Thesis:
    with open(path, "rb") as f:
        raw = tomllib.load(f)
    t = raw["thesis"]
    scenarios = tuple(
        Scenario(s["name"], Decimal(s["price"]), Decimal(s["probability"]))
        for s in raw["scenario"]
    )
    return Thesis(
        ticker=t["ticker"],
        rating=t["rating"],
        price_date=t["price_date"],
        price=Decimal(t["price"]),
        price_target=Decimal(t["price_target"]),
        scenarios=scenarios,
    )
