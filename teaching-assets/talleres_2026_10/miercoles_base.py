"""Completa el experimento 1 y dos electivos del laboratorio del miércoles.

Se pueden reutilizar rutinas propias de clase. Esta es una plantilla,
no un programa que produzca la entrega sin modificaciones. Completa solo
las funciones de tus elecciones; duales y Lagrange son ampliaciones.
"""
import numpy as np
from miercoles_apoyo import (
    Contador, formulas, interpolante_baricentrico, jacobi, potencias,
    datos_lu, seccion_aurea,
)


def mi_kahan(valores):
    raise NotImplementedError("Implementa la acumulación compensada")


def central(f, x, h):
    raise NotImplementedError("Implementa la diferencia central")


def richardson(f, x, h):
    raise NotImplementedError("Combina central con h y h/2")


def dual_suma(a, b):
    raise NotImplementedError("Devuelve el par valor/derivada")


def dual_producto(a, b):
    raise NotImplementedError("Aplica la regla del producto a dos pares")


def adelante(L, b):
    raise NotImplementedError("Sustitución hacia adelante")


def atras(U, b):
    raise NotImplementedError("Sustitución hacia atrás")


def mi_biseccion(f, a, b, tol_x=1e-10, tol_f=1e-10, max_iter=100):
    """Controla signo, raíces en extremos y ambas tolerancias.
    Devuelve raíz, residuo, iteraciones y estado de convergencia.
    Cuenta las evaluaciones envolviendo f con Contador.
    """
    raise NotImplementedError("Completa y prueba la búsqueda")


def lagrange(xs, ys, x):
    raise NotImplementedError("Evalúa los productos cardinales")


def ajuste_normal(xs, ys, grado):
    """Coeficientes en orden creciente: c0, c1, ..."""
    raise NotImplementedError("Forma diseño y ecuaciones normales")


if __name__ == "__main__":
    pasos = 10.0 ** (-np.arange(1, 13))
    malla = np.linspace(-1, 1, 401)
    A, b, P, L, U = datos_lu()
    print("Datos listos. Completa el experimento 1 y dos electivos.")
    print("Pasos:", pasos)
    print("Matriz con pivote inicial nulo:\n", A)
