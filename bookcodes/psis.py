# Author: Alex Gezerlis
# Numerical Methods in Physics with Python (2nd ed., CUP, 2023)

from math import sqrt, pi, factorial, exp
import cmath


def hermite(n, x):
    val0 = 1.
    val1 = 2*x
    for j in range(1, n):
        val2 = 2*x*val1 - 2*j*val0
        val0, val1 = val1, val2
    dval2 = 2*n*val0
    return val2, dval2


def psiqho(x, nametoval):
    n = nametoval["n"]
    momohbar = nametoval["momohbar"]
    al = nametoval["al"]
    psival = momohbar**0.25*exp(-0.5*al*momohbar * x**2)
    psival *= hermite(n, sqrt(momohbar)*x)[0]
    psival /= sqrt(2**n * factorial(n) * sqrt(pi))
    return psival


def psibox(x, nametoval):
    n = nametoval["n"]
    boxl = nametoval["boxl"]
    return cmath.exp(2*pi*n*x*1j/boxl) / sqrt(boxl)


if __name__ == '__main__':
    x = 1.
    ho = {"n": 100, "momohbar": 1., "al": 1.}
    psiA = psiqho(x, ho)
    pb = {"n": -2, "boxl": 2*pi}
    psiB = psibox(x, pb)
    print(psiA, psiB)
    import matplotlib.pyplot as plt
    from numpy import linspace
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(
        12, 5), constrained_layout=True)
    x2 = linspace(-15, 15, 12000)
    yho = [psiqho(i, ho) for i in x2]
    ypb = [psibox(i, pb).real for i in x2]
    ypb2 = [psibox(i, pb).imag for i in x2]
    axs[0].plot(x2, yho, 'b-', label="Oscilador Armónico")
    axs[0].plot(x2, ypb, 'r--', label="Caja de Potencial - Componente Real")
    axs[0].plot(x2, ypb2, 'k-.',
                label="Caja de Potencial - Componente Imaginario")
    axs[0].set_xlabel(r'$x$')
    axs[0].set_ylabel(r'$\psi(x)$')
    axs[0].legend()

    yho_abs = [abs(psiqho(i, ho))**2 for i in x2]
    ypb_abs = [abs(psibox(i, pb))**2 for i in x2]
    axs[1].plot(x2, yho_abs, 'b-', label="Oscilador Armónico")
    axs[1].plot(x2, ypb_abs, 'r--', label="Caja de Potencial")
    axs[1].set_xlabel(r'$x$')
    axs[1].set_ylabel(r'$|\psi(x)|^2$')
    axs[1].legend()
    plt.show()
