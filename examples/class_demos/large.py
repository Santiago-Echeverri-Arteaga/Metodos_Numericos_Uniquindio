"""Experimento sobre absorción de incrementos pequeños en punto flotante."""

from collections.abc import Iterator


def halving_experiment(
    start: float = 2.0**-50, steps: int = 30
) -> Iterator[tuple[int, float, float]]:
    """Produce ``(paso, 1 + incremento, incremento)`` al dividir por dos."""
    increment = start
    for step in range(steps):
        increment /= 2.0
        yield step, 1.0 + increment, increment


def first_absorbed_step(start: float = 2.0**-50, steps: int = 30) -> int | None:
    """Devuelve el primer paso para el que ``1 + incremento == 1``."""
    for step, represented, _ in halving_experiment(start, steps):
        if represented == 1.0:
            return step
    return None


def main() -> None:
    for step, represented, increment in halving_experiment():
        print(step, represented, increment)


if __name__ == "__main__":
    main()
