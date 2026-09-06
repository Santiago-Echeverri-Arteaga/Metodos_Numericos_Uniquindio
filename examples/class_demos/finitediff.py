from math import exp, sin, cos


def f(x):
    return exp(sin(2*x))


def fprime(x):
    return 2*exp(sin(2*x))*cos(2*x)


def calcfd(f, x, h):
    fd = (f(x+h) - f(x))/h
    return fd


def calccd(f, x, h):
    cd = (f(x+h/2) - f(x-h/2))/h
    return cd


if __name__ == '__main__':
    x = 0.5
    an = fprime(x)
    hs = [10**(-i) for i in range(1, 12)]
    fds = [abs(calcfd(f, x, h) - an) for h in hs]
    cds = [abs(calccd(f, x, h) - an) for h in hs]
    rowf = "{0:1.0e}{1:20.16f} {2:20.16f}"
    print("{0:10} {1:17} {2:20}".format(
        'h abs.', 'error in fd', 'abs. error in cd'))
    for h, fd, cd in zip(hs, fds, cds):
        print(rowf.format(h, fd, cd))

    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(
        nrows=1, ncols=1, figsize=(6, 5), constrained_layout=True)
    axs.set_xscale('log')
    axs.set_yscale('log')

    axs.plot(hs, fds, marker="o", label="Diferencia hacia adelante")
    axs.plot(hs, cds, ls="--", marker="^", label="Diferencia central")
    axs.legend(loc=0)
    axs.set_ylabel(r"$|\text{abs. error}|$", size=14)
    axs.set_xlabel(r"$h$", size=14)
    plt.grid(True)
    plt.show()
