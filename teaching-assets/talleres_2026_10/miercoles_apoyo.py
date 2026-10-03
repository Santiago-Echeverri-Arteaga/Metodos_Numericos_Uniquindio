"""Apoyo de cálculo para el miércoles, no informe de respuestas.

Ejecutar: python miercoles_apoyo.py
Requiere NumPy, ya incluido en las dependencias del curso.
Las salidas numéricas deben interpretarse con el enunciado.
"""
from math import cos, exp, pi, sqrt
import numpy as np


def suma_ordinaria(valores):
    total = 0.0
    for valor in valores:
        total += valor
    return total


def kahan(valores):
    total = compensacion = 0.0
    for valor in valores:
        corregido = valor - compensacion
        nuevo = total + corregido
        compensacion = (nuevo - total) - corregido
        total = nuevo
    return total


def formulas(f, x, h):
    derecha = (f(x+h)-f(x))/h
    izquierda = (f(x)-f(x-h))/h
    return {
        "derecha 2 puntos": derecha,
        "izquierda 2 puntos": izquierda,
        "central": (f(x+h)-f(x-h))/(2*h),
        "derecha 3 puntos": (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h),
        "izquierda 3 puntos": (3*f(x)-4*f(x-h)+f(x-2*h))/(2*h),
        "semisuma": (derecha+izquierda)/2,
    }


def interpolante_baricentrico(xs, ys):
    pesos = []
    for i, xi in enumerate(xs):
        producto = 1.0
        for j, xj in enumerate(xs):
            if j != i:
                if xi == xj:
                    raise ValueError("Nodos repetidos")
                producto *= xi-xj
        pesos.append(1.0/producto)

    def evaluar(x):
        for xi, yi in zip(xs, ys):
            if x == xi:
                return yi
        terminos = [w/(x-xi) for w, xi in zip(pesos, xs)]
        return sum(t*y for t, y in zip(terminos, ys))/sum(terminos)
    return evaluar


class Contador:
    def __init__(self, funcion):
        self.funcion = funcion
        self.llamadas = 0

    def __call__(self, *args):
        self.llamadas += 1
        return self.funcion(*args)


def datos_lu():
    A = np.array([[0., 2., 1.], [2., 1., 0.], [1., 0., 2.]])
    b = np.array([7., 4., 7.])
    P = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 1.]])
    L = np.array([[1., 0., 0.], [0., 1., 0.], [.5, -.25, 1.]])
    U = np.array([[2., 1., 0.], [0., 2., 1.], [0., 0., 2.25]])
    return A, b, P, L, U


def jacobi(A, b, tol=1e-8, max_iter=200):
    A, b = np.asarray(A, dtype=float), np.asarray(b, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0):
        raise ValueError("Jacobi necesita una diagonal no nula")
    resto = A-np.diag(diagonal)
    x = np.zeros_like(b)
    historial = []
    for k in range(1, max_iter+1):
        nuevo = (b-resto@x)/diagonal
        residuo = float(np.max(np.abs(A@nuevo-b)))
        cambio = float(np.max(np.abs(nuevo-x)))
        historial.append((k, residuo, cambio))
        x = nuevo
        if not np.all(np.isfinite(x)):
            return x, False, historial
        if residuo <= tol and cambio <= tol:
            return x, True, historial
    return x, False, historial


def potencias(A, tol=1e-8, max_iter=200):
    A = np.asarray(A, dtype=float)
    v = np.zeros(A.shape[0]); v[0] = 1.0
    historial = []
    for k in range(1, max_iter+1):
        w = A@v
        escala = np.max(np.abs(w))
        if escala == 0:
            raise ValueError("El vector inicial fue enviado al vector cero")
        v = w/escala
        valor = float(v@A@v/(v@v))
        residuo = float(np.max(np.abs(A@v-valor*v)))
        historial.append((k, valor, residuo))
        if residuo <= tol:
            return valor, v, True, historial
    return valor, v, False, historial


def seccion_aurea(f, a, b, tol=1e-10, max_iter=100):
    razon = (sqrt(5)-1)/2
    c, d = b-razon*(b-a), a+razon*(b-a)
    fc, fd = f(c), f(d)
    for k in range(max_iter+1):
        if (b-a)/2 <= tol:
            return (a+b)/2, True, k
        if k == max_iter:
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b-razon*(b-a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a+razon*(b-a); fd = f(d)
    return (a+b)/2, False, max_iter


def sistema_no_lineal(metodo="newton", max_iter=50, tol=1e-10):
    """Caso adicional: F=(x²+y-3,x+y²-3), Broyden sobre el jacobiano."""
    if metodo not in ("newton", "broyden"):
        raise ValueError("Elige newton o broyden")
    F = lambda s: np.array([s[0]**2+s[1]-3, s[0]+s[1]**2-3])
    s = np.ones(2)
    B = np.array([[2., 1.], [1., 2.]])
    historial = []
    for k in range(max_iter):
        antes = F(s)
        if np.max(np.abs(antes)) <= tol:
            return s, True, historial
        if metodo == "newton":
            B = np.array([[2*s[0], 1.], [1., 2*s[1]]])
        delta = np.linalg.solve(B, -antes)
        nuevo = s+delta
        despues = F(nuevo)
        historial.append((k+1, float(np.max(np.abs(despues)))))
        if metodo == "broyden" and delta@delta > 0:
            B += np.outer(despues-antes-B@delta, delta)/(delta@delta)
        s = nuevo
    return s, bool(np.max(np.abs(F(s))) <= tol), historial


def main():
    print("Apoyo del laboratorio computacional del miércoles")
    print("Importa este módulo desde miercoles_base.py y completa tus experimentos.")
    print("Funciones disponibles: formulas, interpolante_baricentrico, Contador,")
    print("datos_lu, jacobi, potencias, seccion_aurea y sistema_no_lineal.")
    A, b, P, L, U = datos_lu()
    print("Control de datos PA=LU:", np.allclose(P@A, L@U))


if __name__ == "__main__":
    main()
