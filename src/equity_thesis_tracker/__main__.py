from equity_thesis_tracker.thesis import load_thesis


def main() -> None:
    t = load_thesis()
    print(f"{t.ticker} {t.rating} | price {t.price} on {t.price_date} | target {t.price_target}")
    print(f"probability-weighted value: {t.expected_value()}")
    print(f"price return to target: {t.implied_return()}")
    print(f"position return ({t.rating}): {t.position_return()}")
    for name, r in t.scenario_returns().items():
        print(f"  {name}: {r}")


if __name__ == "__main__":
    main()
