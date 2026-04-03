import numpy as np
from scipy.optimize import root


def fs(xs):
    x0, x1 = xs
    f0 = x0**2 - 2*x0 + x1**4 - 2*x1**2 + x1
    f1 = x0**2 + x0 + 2*x1**3 - 2*x1**2 - 1.5*x1 - 0.05
    return np.array([f0, f1])


def termcrit(xolds, xnews):
    errs = np.abs((xnews - xolds) / xnews)
    return np.sum(errs)


def jacobian_fd(fs, xs, h=1.e-4):
    n = xs.size
    iden = np.identity(n)
    Jf = np.zeros((n, n))
    fs0 = fs(xs)

    for j in range(n):
        fs1 = fs(xs + iden[:, j] * h)
        Jf[:, j] = (fs1 - fs0) / h

    return Jf


def broyden_basic(fs, J0, xolds, kmax=200, tol=1.e-8):
    xolds = np.array(xolds, dtype=float)
    Jolds = np.array(J0, dtype=float)

    for k in range(1, kmax):
        fs_xolds = fs(xolds)
        step = np.linalg.solve(Jolds, -fs_xolds)
        xnews = xolds + step

        err = termcrit(xolds, xnews)
        fs_xnews = fs(xnews)

        print(k, xnews, err, fs_xnews)

        if err < tol:
            break

        q = xnews - xolds
        Jnews = Jolds + np.outer(fs_xnews, q) / (q @ q)

        xolds = np.copy(xnews)
        Jolds = np.copy(Jnews)
    else:
        xnews = None

    return xnews


if __name__ == "__main__":
    x0 = np.array([1.0, 1.0])

    print("Caso 1: J(x^(0)) = I")
    J0 = np.identity(2)
    sol_broyden = broyden_basic(fs, J0, x0)

    # Refinamiento local con SciPy desde la solución hallada por Broyden
    sol_ref = root(fs, sol_broyden, method="hybr").x

    print("Broyden         =", sol_broyden)
    print("Referencia      =", sol_ref)
    print("||dx||_2        =", np.linalg.norm(sol_broyden - sol_ref))
    print("||f(Broyden)||_2=", np.linalg.norm(fs(sol_broyden)))
    print("||f(ref)||_2    =", np.linalg.norm(fs(sol_ref)))
    print()

    print("Caso 2: J(x^(0)) por forward difference")
    J0 = jacobian_fd(fs, x0)
    sol_broyden = broyden_basic(fs, J0, x0)

    sol_ref = root(fs, sol_broyden, method="hybr").x

    print("Broyden         =", sol_broyden)
    print("Referencia      =", sol_ref)
    print("||dx||_2        =", np.linalg.norm(sol_broyden - sol_ref))
    print("||f(Broyden)||_2=", np.linalg.norm(fs(sol_broyden)))
    print("||f(ref)||_2    =", np.linalg.norm(fs(sol_ref)))
