"""Extrapolación de Richardson aplicada a diferencias finitas."""

from collections.abc import Callable, Iterable

try:
    from .finitediff import calcfd, calccd, f, fprime
except ImportError:  # Permite ejecutar este archivo directamente.
    from finitediff import calcfd, calccd, f, fprime


ScalarFunction = Callable[[float], float]


def richardson_forward(function: ScalarFunction, x: float, h: float) -> float:
    """Eleva de orden uno a orden dos una diferencia hacia adelante."""
    return 2.0 * calcfd(function, x, h / 2.0) - calcfd(function, x, h)


def richardson_central(function: ScalarFunction, x: float, h: float) -> float:
    """Eleva de orden dos a orden cuatro una diferencia central."""
    return (4.0 * calccd(function, x, h / 2.0) - calccd(function, x, h)) / 3.0


def error_table(
    function: ScalarFunction,
    derivative: ScalarFunction,
    x: float,
    steps: Iterable[float],
) -> list[tuple[float, float, float]]:
    """Calcula errores absolutos para ambas extrapolaciones."""
    exact = derivative(x)
    return [
        (
            h,
            abs(richardson_forward(function, x, h) - exact),
            abs(richardson_central(function, x, h) - exact),
        )
        for h in steps
    ]


def main() -> None:
    rows = error_table(f, fprime, x=0.5, steps=(10.0**-i for i in range(1, 7)))
    print(f"{'h':10} {'error rich fd':20} {'error rich cd':20}")
    for h, forward_error, central_error in rows:
        print(f"{h:1.0e} {forward_error:20.16f} {central_error:20.16f}")


if __name__ == "__main__":
    main()
