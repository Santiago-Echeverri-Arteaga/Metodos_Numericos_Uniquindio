# Unidad 3. Álgebra lineal numérica

## Sentido de la unidad

Muchos modelos físicos terminan en un sistema lineal, un problema de valores propios o una operación matricial. La forma matemática `Ax=b` parece compacta, pero su solución numérica depende de la estructura de `A`, de su condicionamiento, del método elegido y de los errores acumulados.

Esta unidad estudia cómo resolver sistemas sin calcular explícitamente la inversa, cómo medir la calidad de la respuesta y cómo elegir entre métodos directos e iterativos.

> **Lectura orientadora:** notas de clase, apartados de matrices, sistemas triangulares, eliminación gaussiana, factorización, Jacobi y método de potencias; Gezerlis, capítulo 4.

## Resultados de aprendizaje

Al terminar la unidad, el estudiante podrá:

- utilizar normas vectoriales y matriciales para cuantificar magnitudes y errores;
- interpretar el número de condición;
- resolver sistemas triangulares por sustitución;
- implementar eliminación gaussiana con pivoteo;
- explicar la factorización LU y su utilidad;
- aplicar métodos iterativos básicos y analizar su convergencia;
- calcular un valor propio dominante mediante el método de potencias;
- verificar soluciones mediante residuos y reconstrucciones.

## Secuencia sugerida de clases

| Clase | Pregunta central | Métodos | Evidencia |
| --- | --- | --- | --- |
| 1 | ¿Cómo medir vectores, matrices y perturbaciones? | Normas, residuo y condición | Experimento de sensibilidad |
| 2 | ¿Cómo se aprovecha una matriz triangular? | Sustitución hacia adelante y atrás | Funciones verificadas |
| 3 | ¿Cómo transformar un sistema general? | Eliminación gaussiana y pivoteo | Traza de operaciones |
| 4 | ¿Cómo reutilizar el trabajo para varios vectores `b`? | LU | Reconstrucción `PA≈LU` |
| 5 | ¿Cuándo conviene iterar? | Jacobi y Gauss-Seidel | Historia de residuos |
| 6 | ¿Cómo obtener estados o modos característicos? | Potencias y cociente de Rayleigh | Valor propio y residuo |

## 1. Del modelo físico al sistema lineal

Un sistema se escribe como:

A x = b

| Elemento | Interpretación |
| --- | --- |
| `A` | Relaciones entre incógnitas; puede contener geometría, acoplamientos o discretización |
| `x` | Cantidades desconocidas |
| `b` | Fuentes, condiciones o mediciones conocidas |

Ejemplos físicos incluyen redes de resistencias, balances de fuerzas, ajustes lineales, discretización de ecuaciones diferenciales y expansión en una base.

## 2. Normas y residuo

Una norma permite medir el tamaño de un vector o una matriz. Para una aproximación `x_aprox`, el residuo es:

r = b - A x_aprox

| Métrica | Qué informa | Limitación |
| --- | --- | --- |
| Error absoluto `||x_aprox - x||` | Distancia a la solución exacta | Requiere conocer la solución exacta |
| Norma del residuo `||r||` | Cumplimiento del sistema | Puede ser pequeña en sistemas mal condicionados |
| Error relativo | Error comparado con la escala | Depende de la norma elegida |
| Error hacia atrás | Perturbación mínima que justificaría la respuesta | Su interpretación exige contexto |

El residuo siempre debe acompañarse de una escala. Un valor `10⁻⁶` puede ser grande o pequeño según `||A||`, `||x||` y `||b||`.

## 3. Condicionamiento

El número de condición estima cuánto puede amplificarse una perturbación relativa de los datos:

κ(A) = ||A|| · ||A⁻¹||

No es necesario ni recomendable formar `A⁻¹` para resolver el sistema. Las bibliotecas calculan o estiman la condición mediante algoritmos especializados.

| Valor cualitativo de `κ(A)` | Interpretación |
| --- | --- |
| Cercano a 1 | Perturbaciones pequeñas suelen permanecer pequeñas |
| Moderado | Se pierden algunas cifras significativas |
| Muy grande | La solución puede ser extremadamente sensible |
| Infinito o matriz singular | No existe solución única |

La condición depende también de la norma y del escalamiento de variables. Antes de concluir que un modelo es intrínsecamente malo, revise si las variables mezclan escalas o unidades incompatibles.

## 4. Sistemas triangulares

Si `L` es triangular inferior, la solución se obtiene desde la primera ecuación hacia la última. Si `U` es triangular superior, se procede en sentido inverso.

```python
def sustitucion_atras(U, b):
    n = len(b)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += U[i][j] * x[j]
        x[i] = (b[i] - suma) / U[i][i]

    return x
```

Una implementación completa debe detectar pivotes nulos o demasiado pequeños y verificar dimensiones compatibles.

## 5. Eliminación gaussiana y pivoteo

La eliminación transforma `A` en una matriz triangular mediante operaciones elementales sobre filas. Luego se aplica sustitución hacia atrás.

| Etapa | Objetivo | Riesgo numérico |
| --- | --- | --- |
| Selección de pivote | Elegir el elemento divisor | Dividir por cero o por un valor muy pequeño |
| Eliminación | Anular entradas bajo el pivote | Acumular redondeo y pérdida de escala |
| Sustitución | Recuperar las incógnitas | Propagar error desde las últimas ecuaciones |

El pivoteo parcial intercambia filas para elegir, dentro de la columna activa, un elemento de mayor magnitud. Esta estrategia suele mejorar la estabilidad y debe formar parte del algoritmo general.

### Evidencia de corrección

No basta con comparar `x` visualmente. Calcule:

- el residuo `b-Ax`;
- el residuo relativo;
- la diferencia frente a `numpy.linalg.solve` en casos de prueba;
- el comportamiento ante matrices singulares o casi singulares.

## 6. Factorización LU

La eliminación puede expresarse mediante una factorización:

P A = L U

`P` representa los intercambios de fila, `L` es triangular inferior y `U` triangular superior. Para resolver varios sistemas con la misma `A` y diferentes vectores `b`, se factoriza una vez y luego se realizan sustituciones.

| Escenario | Estrategia conveniente |
| --- | --- |
| Un solo sistema denso pequeño | `solve` o eliminación con pivoteo |
| Muchos vectores `b` con la misma `A` | Factorizar una vez y reutilizar |
| Matriz simétrica definida positiva | Cholesky, si se han verificado las condiciones |
| Matriz grande y dispersa | Método y estructura de datos especializados |
| Ajuste por mínimos cuadrados | QR o SVD en lugar de ecuaciones normales cuando la estabilidad importa |

## 7. Métodos iterativos

En Jacobi, cada componente de la nueva aproximación se calcula usando exclusivamente los valores de la iteración anterior. Gauss-Seidel reutiliza de inmediato los valores ya actualizados.

```python
import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=500):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    x = np.asarray(x0, dtype=float).copy()
    diagonal = np.diag(A)
    resto = A - np.diagflat(diagonal)
    historial = []

    for _ in range(max_iter):
        nuevo = (b - resto @ x) / diagonal
        residuo = np.linalg.norm(b - A @ nuevo)
        historial.append(residuo)
        if residuo <= tol:
            return nuevo, historial
        x = nuevo

    raise RuntimeError("Jacobi no alcanzó la tolerancia")
```

El método no converge para cualquier matriz. La dominancia diagonal es una condición suficiente útil, pero no necesaria. Un análisis más general estudia el radio espectral de la matriz de iteración.

## 8. Valores propios y método de potencias

Los valores propios aparecen en modos normales, energías permitidas, estabilidad y dinámica lineal:

A v = λ v

El método de potencias aplica repetidamente `A` a un vector y lo normaliza. Bajo condiciones apropiadas, la dirección converge al vector propio asociado al valor propio de mayor magnitud.

### Diagnósticos

- residuo propio `||Av-λv||`;
- cambio del cociente de Rayleigh;
- sensibilidad a la aproximación inicial;
- presencia de valores propios dominantes con igual magnitud;
- comparación con `numpy.linalg.eig` o `eigh` cuando corresponda.

## 9. Aplicaciones físicas

| Aplicación | Objeto matricial | Resultado |
| --- | --- | --- |
| Rotaciones | Matriz ortogonal | Cambio de coordenadas sin alterar norma |
| Momento de inercia | Tensor simétrico | Ejes principales y momentos propios |
| Sistemas acoplados | Matriz dinámica | Frecuencias y modos normales |
| Espín | Operadores matriciales | Estados y resultados posibles |
| Schrödinger discretizada | Hamiltoniano | Energías y estados propios |

En matrices simétricas o hermíticas conviene usar algoritmos que aprovechen esa estructura; las soluciones deberían reflejar valores propios reales y vectores propios ortogonales dentro de la precisión numérica.

## Errores frecuentes

| Error | Por qué es problemático | Alternativa |
| --- | --- | --- |
| Calcular `inv(A) @ b` | Es más costoso y suele ser menos estable | Usar `solve(A, b)` |
| Omitir pivoteo | Puede dividir por números pequeños | Pivoteo parcial |
| Usar solo `||x_{k+1}-x_k||` | Puede confundir estancamiento con convergencia | Revisar también `||b-Ax||` |
| Ignorar escala de variables | Empeora interpretación y condición | Reescalar con criterio físico |
| Aplicar Jacobi sin revisar convergencia | Puede divergir | Analizar matriz e historial |
| Aceptar un valor propio sin residuo | La normalización no prueba corrección | Calcular `||Av-λv||` |

## Taller propuesto

1. Implemente sustitución hacia adelante y atrás; pruebe matrices de tamaños 2, 3 y 5.
2. Cuente operaciones dominantes de la eliminación y de la sustitución.
3. Implemente eliminación gaussiana sin pivoteo y construya un caso que falle.
4. Añada pivoteo parcial y registre los intercambios.
5. Compruebe `PA≈LU` y compare varios vectores `b`.
6. Perturbe ligeramente una matriz bien condicionada y una casi singular; compare soluciones.
7. Implemente Jacobi y grafique residuo contra iteración.
8. Compare Jacobi y Gauss-Seidel en una matriz diagonalmente dominante.
9. Use el método de potencias en una matriz simétrica con valores propios conocidos.
10. Discretice un operador de segunda derivada y explore sus primeros valores propios.

## Producto integrador de la unidad

Resuelva un problema físico lineal mediante dos estrategias. El informe debe incluir la construcción de `A` y `b`, interpretación de unidades, condición estimada, solución, residuo, comparación entre métodos y una perturbación controlada de los datos.

## Lista de comprobación

- [ ] No calculé la inversa explícita para resolver `Ax=b`.
- [ ] Verifiqué dimensiones y estructura de la matriz.
- [ ] Incluí pivoteo cuando corresponde.
- [ ] Reporté un residuo escalado.
- [ ] Estimé o discutí el condicionamiento.
- [ ] Registré convergencia en métodos iterativos.
- [ ] Para valores propios, comprobé `Av≈λv`.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados de matrices, sistemas lineales y problemas propios.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 4 y apéndice C.2.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
