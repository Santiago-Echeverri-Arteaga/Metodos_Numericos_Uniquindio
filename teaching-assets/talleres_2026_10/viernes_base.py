"""Plantilla del viernes: Python estándar. No contiene la solución.

Completa las dos rutinas y el recorrido del enunciado. En A puedes
conectarlas a librerías; en B entrega tus implementaciones.
"""
from math import cos, pi, sqrt

ALPHA = 4
Q = 0.30
L = 0.02  # m
E0 = 0.10  # J
NODOS = "chebyshev"  # o "uniformes"


def energia(z, alpha=ALPHA, q=Q):
    return alpha * z * z / (sqrt(1 + alpha * z * z) + 1) - q * z


def generar_nodos(tipo=NODOS):
    if tipo == "uniformes":
        return [-1 + i / 4 for i in range(9)]
    if tipo == "chebyshev":
        return [-cos(i * pi / 8) for i in range(9)]
    raise ValueError("Elige uniformes o chebyshev")


def normales(zs, ys, grado, acumular=sum):
    matriz = [[acumular([z ** (j + k) for z in zs])
               for k in range(grado + 1)] for j in range(grado + 1)]
    rhs = [acumular([y * z ** j for z, y in zip(zs, ys)])
           for j in range(grado + 1)]
    return matriz, rhs


def polinomio(coef, z):
    """Coeficientes en orden c0,c1,...; admite también un número dual."""
    valor = 0.0
    for c in reversed(coef):
        valor = valor * z + c
    return valor


def coef_derivada(coef):
    return [i * coef[i] for i in range(1, len(coef))]


def central(f, z, h):
    return (f(z + h) - f(z - h)) / (2 * h)


def richardson(f, z, h=0.01):
    return (4 * central(f, z, h / 2) - central(f, z, h)) / 3


def segunda(f, z, h):
    return (f(z + h) - 2 * f(z) + f(z - h)) / h ** 2


def residuo_sistema(matriz, coef, rhs):
    return max(abs(sum(a * c for a, c in zip(fila, coef)) - b)
               for fila, b in zip(matriz, rhs))


def resolver(matriz, rhs):
    """B: eliminación con pivoteo parcial y sustitución hacia atrás.
    Devuelve coeficientes sin modificar entradas. Controla los pivotes
    con un criterio relativo a la escala de la matriz.
    """
    raise NotImplementedError("Completa o conecta tu solucionador")


def construir_interpolante(zs, ys):
    """Apoyo suministrado para A y B: fórmula baricéntrica estándar."""
    if len(zs) != len(ys) or not len(zs):
        raise ValueError("Datos vacíos o tamaños incompatibles")
    pesos = []
    for i, zi in enumerate(zs):
        producto = 1.0
        for j, zj in enumerate(zs):
            if i != j:
                if zi == zj:
                    raise ValueError("Nodos repetidos")
                producto *= zi-zj
        pesos.append(1.0/producto)

    def evaluar(z):
        for zi, yi in zip(zs, ys):
            if z == zi:
                return yi
        terminos = [w/(z-zi) for w, zi in zip(pesos, zs)]
        return sum(t*y for t, y in zip(terminos, ys))/sum(terminos)
    return evaluar


def biseccion(f, a, b, tol_x=1e-7, tol_f=1e-7, max_iter=100):
    """Devuelve dict: raiz, intervalo, residuo, iteraciones, evaluaciones,
    convergio. Exige ambas tolerancias; acepta raíces en extremos y
    rechaza un intervalo sin cambio de signo.
    """
    raise NotImplementedError("Completa tu bisección")


if __name__ == "__main__":
    assert ALPHA in (1, 4, 9) and Q in (0.20, 0.30, 0.40)
    zs = generar_nodos()
    ys = [energia(z) for z in zs]
    comprobacion = [-1 + (j + 0.5) / 20 for j in range(40)]
    print("alpha, q, nodos:", ALPHA, Q, NODOS)
    print("Fuerza aplicada (N):", Q * E0 / L)
    print("Muestras (z,u):", list(zip(zs, ys)))
    for grado in (4,):
        matriz, rhs = normales(zs, ys, grado)
        print("Sistema del grado", grado, matriz, rhs)
    print("Completa: aproximaciones, equilibrio y decisión.")
