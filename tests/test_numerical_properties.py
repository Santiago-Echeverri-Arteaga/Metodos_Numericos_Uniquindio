"""Pruebas pequeñas que expresan propiedades enseñadas en el curso."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "examples" / "class_demos"


def load_demo(name: str):
    """Load a demonstration without requiring it to be a Python package."""
    path = DEMOS / f"{name}.py"
    if str(DEMOS) not in sys.path:
        sys.path.insert(0, str(DEMOS))
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NumericalPropertiesTest(unittest.TestCase):
    def test_compensated_sum_represents_decimal_example_better(self):
        demo = load_demo("suma_kahan")
        values = [0.7, 0.1, 0.3]
        compensated_error = abs(demo.kahan_sum(values) - 1.1)
        ordinary_error = abs(sum(values) - 1.1)
        self.assertTrue(math.isclose(demo.kahan_sum(values), 1.1))
        self.assertLessEqual(compensated_error, ordinary_error)

    def test_small_increment_is_eventually_absorbed(self):
        demo = load_demo("large")
        self.assertEqual(demo.first_absorbed_step(), 2)

    def test_central_difference_has_smaller_error(self):
        demo = load_demo("finitediff")
        x = 0.5
        h = 1e-3
        exact = demo.fprime(x)
        forward_error = abs(demo.calcfd(demo.f, x, h) - exact)
        central_error = abs(demo.calccd(demo.f, x, h) - exact)
        self.assertLess(central_error, forward_error)

    def test_forward_difference_displays_first_order_convergence(self):
        demo = load_demo("finitediff")
        x = 0.5
        exact = demo.fprime(x)
        coarse = abs(demo.calcfd(demo.f, x, 1e-3) - exact)
        fine = abs(demo.calcfd(demo.f, x, 5e-4) - exact)
        self.assertTrue(math.isclose(coarse / fine, 2.0, rel_tol=0.02))

    def test_richardson_central_improves_the_central_difference(self):
        finite = load_demo("finitediff")
        richardson = load_demo("richardsondiff")
        x = 0.5
        h = 0.1
        exact = finite.fprime(x)
        base_error = abs(finite.calccd(finite.f, x, h) - exact)
        improved_error = abs(richardson.richardson_central(finite.f, x, h) - exact)
        self.assertLess(improved_error, base_error)

    def test_ridder_finds_a_bracketed_root(self):
        demo = load_demo("Ridder")
        root = demo.ridders(demo.f, 2.0, 3.0)
        self.assertLess(abs(demo.f(root)), 1e-10)

    def test_ridder_rejects_an_unbracketed_interval(self):
        demo = load_demo("Ridder")
        with self.assertRaises(ValueError):
            demo.ridders(lambda x: x * x + 1.0, -1.0, 1.0)

    @unittest.skipUnless(
        importlib.util.find_spec("numpy") is not None,
        "NumPy se instala mediante las dependencias del proyecto",
    )
    def test_broyden_requires_small_step_and_residual(self):
        import numpy as np

        demo = load_demo("Broyden")
        x0 = np.array([1.0, 1.0])
        solution = demo.broyden_basic(
            demo.fs,
            demo.jacobian_fd(demo.fs, x0),
            x0,
            kmax=200,
        )
        self.assertLess(np.linalg.norm(demo.fs(solution)), 1e-8)


if __name__ == "__main__":
    unittest.main()
