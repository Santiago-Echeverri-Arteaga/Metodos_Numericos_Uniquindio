from math import exp, sqrt, copysign
from scipy.optimize import root_scalar


def f(x):
    return exp(x - sqrt(x)) - x


def ridders(f, x0, x1, kmax=200, tol=1.e-8):
    f0 = f(x0)
    f1 = f(x1)

    if f0 == 0.0:
        return x0
    if f1 == 0.0:
        return x1
    if f0 * f1 > 0.0:
        return None

    xold = None

    for k in range(1, kmax):
        x2 = 0.5 * (x0 + x1)
        f2 = f(x2)

        den = sqrt(f2**2 - f0*f1)
        x3 = x2 + copysign(1.0, f0) * f2 * (x2 - x0) / den
        f3 = f(x3)

        if xold is None:
            xdiff = abs(x1 - x0)
        else:
            xdiff = abs(x3 - xold)

        rowf = "{0:2d} {1:1.16f} {2:1.16e} {3:1.16e}"
        print(rowf.format(k, x3, xdiff, abs(f3)))

        if abs(xdiff / x3) < tol:
            break

        if f2 * f3 < 0.0:
            x0, f0 = x2, f2
            x1, f1 = x3, f3
        elif f0 * f3 < 0.0:
            x1, f1 = x3, f3
        else:
            x0, f0 = x3, f3

        xold = x3
    else:
        x3 = None

    return x3


if __name__ == "__main__":
    print("Raíz en (0.0, 1.7)")
    root_rid = ridders(f, 0.0, 1.7)
    root_ref = root_scalar(f, bracket=(0.0, 1.7), method="brentq").root

    print(f"Ridders     = {root_rid:.16f}")
    print(f"Referencia  = {root_ref:.16f}")
    print(f"Error abs   = {abs(root_rid - root_ref):.3e}")
    print(f"|f(Ridders)|= {abs(f(root_rid)):.3e}")
    print()

    print("Raíz en (2.0, 3.0)")
    root_rid = ridders(f, 2.0, 3.0)
    root_ref = root_scalar(f, bracket=(2.0, 3.0), method="brentq").root

    print(f"Ridders     = {root_rid:.16f}")
    print(f"Referencia  = {root_ref:.16f}")
    print(f"Error abs   = {abs(root_rid - root_ref):.3e}")
    print(f"|f(Ridders)|= {abs(f(root_rid)):.3e}")
