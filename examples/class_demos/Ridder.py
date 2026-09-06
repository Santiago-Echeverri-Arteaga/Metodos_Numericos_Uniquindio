"""Implementación docente y robusta del método de Ridder."""

from collections.abc import Callable
from math import copysign, exp, isfinite, sqrt


ScalarFunction = Callable[[float], float]


def f(x: float) -> float:
    return exp(x - sqrt(x)) - x


def ridders(
    function: ScalarFunction,
    x0: float,
    x1: float,
    *,
    kmax: int = 200,
    atol: float = 1e-12,
    rtol: float = 1e-8,
    ftol: float = 1e-10,
    verbose: bool = False,
) -> float:
    """Encuentra una raíz dentro de un intervalo con cambio de signo.

    El criterio exige un residuo pequeño o un cambio entre iteraciones compatible con
    tolerancias absoluta y relativa. Se rechazan intervalos sin bracket y estados no
    finitos en lugar de devolver silenciosamente un resultado dudoso.
    """
    f0 = function(x0)
    f1 = function(x1)

    if not all(isfinite(value) for value in (f0, f1)):
        raise ValueError("La función debe ser finita en los extremos del intervalo")
    if abs(f0) <= ftol:
        return x0
    if abs(f1) <= ftol:
        return x1
    if f0 * f1 > 0.0:
        raise ValueError("El intervalo no encierra un cambio de signo")

    previous: float | None = None

    for iteration in range(1, kmax + 1):
        midpoint = 0.5 * (x0 + x1)
        fmid = function(midpoint)
        radicand = fmid * fmid - f0 * f1

        if not isfinite(fmid) or radicand <= 0.0:
            raise RuntimeError("La actualización de Ridder se volvió degenerada")

        root = midpoint + copysign(1.0, f0) * fmid * (midpoint - x0) / sqrt(
            radicand
        )
        froot = function(root)
        if not isfinite(froot):
            raise RuntimeError("La función produjo un valor no finito")

        change = abs(x1 - x0) if previous is None else abs(root - previous)
        if verbose:
            print(iteration, root, change, abs(froot))

        if abs(froot) <= ftol:
            return root
        if previous is not None and change <= atol + rtol * abs(root):
            return root

        if fmid * froot < 0.0:
            x0, f0 = midpoint, fmid
            x1, f1 = root, froot
        elif f0 * froot < 0.0:
            x1, f1 = root, froot
        elif f1 * froot < 0.0:
            x0, f0 = root, froot
        else:
            return root

        previous = root

    raise RuntimeError(f"Ridder no convergió en {kmax} iteraciones")


def main() -> None:
    from scipy.optimize import root_scalar

    for bracket in ((0.0, 1.7), (2.0, 3.0)):
        root = ridders(f, *bracket, verbose=True)
        reference = root_scalar(f, bracket=bracket, method="brentq").root
        print(f"Ridder      = {root:.16f}")
        print(f"Referencia  = {reference:.16f}")
        print(f"Error abs.  = {abs(root - reference):.3e}")
        print(f"|f(Ridder)| = {abs(f(root)):.3e}\n")


if __name__ == "__main__":
    main()
