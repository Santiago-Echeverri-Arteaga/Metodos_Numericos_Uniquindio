"""Datos y utilidades del proyecto opcional. No entrena ni selecciona modelos.

Instalación en el entorno del curso: python -m pip install -e ".[regresion]"
"""
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

SEMILLA = 42
K = 2.0
BETA = 0.8
SIGMA = 0.08
TAU_OPERACION = 0.0
L = 0.02  # m


def fuerza_sin_ruido(X, k=K, beta=BETA):
    """Solo generación y auditoría final; no usar como respuesta de ajuste."""
    X = np.asarray(X, dtype=float)
    z, tau = X[..., 0], X[..., 1]
    return 0.1+k*z+beta*z**3+0.3*tau*z+0.2*tau


def generar_datos(semilla=SEMILLA, k=K, beta=BETA, sigma=SIGMA):
    if not (0 <= semilla <= 9999 and k in (1.5, 2., 2.5)
            and beta in (.4, .8, 1.2) and sigma in (.03, .08, .15)):
        raise ValueError("Parámetros fuera del alcance del proyecto")
    rng = np.random.default_rng(semilla)
    X = rng.uniform(-1., 1., size=(240, 2))
    y = fuerza_sin_ruido(X, k, beta)+rng.normal(0., sigma, 240)
    return X, y


def particion(n=240):
    return train_test_split(np.arange(n), test_size=.25, random_state=2026)


def crear_busquedas():
    """Objetos SIN ajustar. Llama fit solo con X_ent, y_ent."""
    cv = KFold(n_splits=3, shuffle=True, random_state=2026)
    estimadores = {
        "OLS": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(max_iter=50000, tol=1e-6),
    }
    resultado = {}
    for nombre, estimador in estimadores.items():
        pipeline = Pipeline([
            ("poly", PolynomialFeatures(degree=3, include_bias=False)),
            ("scale", StandardScaler()),
            ("model", estimador),
        ])
        parametros = {}
        if nombre == "Ridge":
            parametros["model__alpha"] = [0.0001, 0.01, 0.1, 1., 10.]
        elif nombre == "Lasso":
            parametros["model__alpha"] = [0.0001, 0.001, 0.003, 0.01, 0.1]
        resultado[nombre] = GridSearchCV(
            pipeline, parametros, scoring="neg_root_mean_squared_error",
            cv=cv, refit=True, n_jobs=1, error_score="raise",
            return_train_score=True,
        )
    return resultado


def coeficientes_originales(pipeline):
    """Coeficientes sobre monomios de (z,tau), sin estandarización.

    Retorna intercepto, exponentes y coeficientes; útil para comparar
    réplicas cuyos StandardScaler tienen medias y escalas diferentes.
    """
    escala = pipeline.named_steps["scale"]
    modelo = pipeline.named_steps["model"]
    coef = np.asarray(modelo.coef_)/escala.scale_
    intercepto = float(modelo.intercept_-coef@escala.mean_)
    potencias = pipeline.named_steps["poly"].powers_.copy()
    return intercepto, potencias, coef


def guardar_datos(ruta, X, y, entrenamiento, prueba):
    """Exporta observaciones e indicadores de partición, sin reajustar."""
    reservado = np.zeros(len(y), dtype=int)
    reservado[prueba] = 1
    assert set(entrenamiento).isdisjoint(prueba)
    np.savetxt(ruta, np.column_stack((np.arange(len(y)), X, y, reservado)),
               delimiter=",", header="id,z,tau,fuerza_N,prueba", comments="")


if __name__ == "__main__":
    X, y = generar_datos()
    ent, test = particion(len(y))
    print("Datos:", X.shape, "entrenamiento:", len(ent), "prueba:", len(test))
    print("Completa: comparación por CV, álgebra, decisión y prueba final.")
    print("Las búsquedas de crear_busquedas() todavía no están ajustadas.")
