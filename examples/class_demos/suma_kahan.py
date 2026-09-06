"""Suma compensada de Kahan y comparación con la suma ordinaria."""

from collections.abc import Iterable


def kahan_sum(values: Iterable[float]) -> float:
    """Suma valores reduciendo la pérdida acumulada por redondeo."""
    total = 0.0
    correction = 0.0

    for value in values:
        adjusted = value - correction
        updated = total + adjusted
        correction = (updated - total) - adjusted
        total = updated

    return total


def main() -> None:
    values = [0.7, 0.1, 0.3]
    print(f"Suma ordinaria: {sum(values):.17g}")
    print(f"Suma de Kahan:  {kahan_sum(values):.17g}")


if __name__ == "__main__":
    main()
