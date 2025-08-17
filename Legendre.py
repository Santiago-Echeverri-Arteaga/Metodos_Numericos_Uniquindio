import matplotlib.pyplot as plt


def legendre(n, x):
    if n == 0:
        val2 = 1.
        dval2 = 0.
    elif n == 1:
        val2 = x
        dval2 = 1.
    else:
        val0 = 1.
        val1 = x
        for j in range(1, n):
            val2 = ((2 * j + 1) * x * val1 - j * val0) / (j + 1)
            val0, val1 = val1, val2
        dval2 = n * (val0 - x * val1) / (1. - x ** 2)
    return val2, dval2


def plot_legendre(ax, der, nsteps):
    ax.set_xlabel('$x$', fontsize=14)
    dertostr = {0: "$P_n(x)$", 1: "$P_n'(x)$"}
    ax.set_ylabel(dertostr[der], fontsize=14)

    ntomarker = {1: 'k-', 2: 'r--', 3: 'b-.', 4: 'g:', 5: 'c'}
    xs = [i / nsteps for i in range(-nsteps + 1, nsteps)]

    for n, marker in ntomarker.items():
        ys = [legendre(n, x)[der] for x in xs]
        labstr = f'n={n}'
        ax.plot(xs, ys, marker, label=labstr, linewidth=2)

    ax.set_ylim(-3 * der - 1, 3 * der + 1)
    ax.legend(loc='lower right')
    ax.grid(True)


def main():
    nsteps = 200
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    plot_legendre(axs[0], der=0, nsteps=nsteps)
    plot_legendre(axs[1], der=1, nsteps=nsteps)
    fig.suptitle('Polinomios de Legendre y sus Derivadas', fontsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()

# from functools import lru_cache


# @lru_cache(maxsize=None)
# def legendre_recursive(n, x):
#    if n == 0:
#        return 1.0
#    elif n == 1:
#        return x
#    else:
#        return ((2 * n - 1) * x * legendre_recursive(n - 1, x) -
#                (n - 1) * legendre_recursive(n - 2, x)) / n
