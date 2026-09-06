"""Método de Broyden con criterios explícitos de paso y residuo."""

from collections.abc import Callable

import numpy as np


VectorFunction = Callable[[np.ndarray], np.ndarray]


def fs(xs: np.ndarray) -> np.ndarray:
    x0, x1 = xs
    f0 = x0**2 - 2 * x0 + x1**4 - 2 * x1**2 + x1
    f1 = x0**2 + x0 + 2 * x1**3 - 2 * x1**2 - 1.5 * x1 - 0.05
    return np.array([f0, f1])


def jacobian_fd(function: VectorFunction, xs: np.ndarray, h: float = 1e-4) -> np.ndarray:
    """Aproxima el jacobiano mediante diferencias hacia adelante."""
    xs = np.asarray(xs, dtype=float)
    identity = np.identity(xs.size)
    jacobian = np.zeros((xs.size, xs.size))
    f0 = function(xs)

    for column in range(xs.size):
        f1 = function(xs + identity[:, column] * h)
        jacobian[:, column] = (f1 - f0) / h

    return jacobian


def broyden_basic(
    function: VectorFunction,
    jacobian0: np.ndarray,
    x0: np.ndarray,
    *,
    kmax: int = 200,
    atol: float = 1e-12,
    rtol: float = 1e-8,
    ftol: float = 1e-8,
    verbose: bool = False,
) -> np.ndarray:
    """Resuelve ``function(x) = 0`` mediante el primer método de Broyden.

    Para aceptar convergencia se exigen simultáneamente un paso pequeño y un residuo
    pequeño. Esto evita confundir estancamiento con solución.
    """
    x_old = np.asarray(x0, dtype=float).copy()
    jacobian_old = np.asarray(jacobian0, dtype=float).copy()

    if np.linalg.norm(function(x_old)) <= ftol:
        return x_old

    for iteration in range(1, kmax + 1):
        f_old = function(x_old)
        step = np.linalg.solve(jacobian_old, -f_old)
        x_new = x_old + step
        f_new = function(x_new)

        step_norm = np.linalg.norm(step)
        residual_norm = np.linalg.norm(f_new)
        step_limit = atol + rtol * np.linalg.norm(x_new)

        if verbose:
            print(iteration, x_new, step_norm, residual_norm)

        if step_norm <= step_limit and residual_norm <= ftol:
            return x_new

        denominator = step @ step
        if denominator <= np.finfo(float).eps:
            raise RuntimeError(
                "Broyden se estancó con un paso nulo y residuo no convergido"
            )

        # y - J s = f(x_new), porque J s = -f(x_old) al resolver el paso.
        jacobian_old = jacobian_old + np.outer(f_new, step) / denominator
        x_old = x_new

    raise RuntimeError(f"Broyden no convergió en {kmax} iteraciones")


def main() -> None:
    from scipy.optimize import root

    x0 = np.array([1.0, 1.0])
    for label, jacobian0 in (
        ("J(x0) = I", np.identity(2)),
        ("J(x0) por diferencia finita", jacobian_fd(fs, x0)),
    ):
        print(label)
        solution = broyden_basic(fs, jacobian0, x0, verbose=True)
        reference = root(fs, solution, method="hybr").x
        print("Broyden          =", solution)
        print("Referencia       =", reference)
        print("||dx||_2         =", np.linalg.norm(solution - reference))
        print("||f(Broyden)||_2 =", np.linalg.norm(fs(solution)), "\n")


if __name__ == "__main__":
    main()
