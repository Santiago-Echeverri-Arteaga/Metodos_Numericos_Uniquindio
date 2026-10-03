# Proyecto opcional: regresión para decidir una posición de operación

**Trabajo individual de consulta y desarrollo · Hasta 3 puntos del segundo parcial**

En este proyecto integraremos los métodos vistos en clase con regresión lineal, Ridge y Lasso. Usaremos datos ruidosos para decidir qué desplazamiento produce una fuerza de **1 N** y justificar la confianza que merece esa decisión.

Se entrega para evaluación antes del segundo parcial. Puedes reutilizar el código del miércoles y viernes; no hay que volver a implementarlo. La [plantilla](regresion_base.py) proporciona datos, partición, pipelines y búsquedas de hiperparámetros ya configuradas. Tu trabajo consiste en ejecutar una comparación válida, explicar el álgebra y verificar la decisión.

**El núcleo obligatorio son las cuatro secciones siguientes.** Las ampliaciones del final no dan puntos ni son necesarias para obtener la máxima valoración o la exoneración.

## 1. Datos y comparación de tres modelos

El generador entrega 240 observaciones simuladas de fuerza en N, con entradas `z=x/L`, `L=0.02 m`, y `tau=(T-25)/10`, con T en °C. Ambas entradas están en [-1,1]. No son mediciones de un dispositivo real.

Elige antes de entrenar:

| Parámetro | Opciones |
| --- | --- |
| Semilla | Entero de 0 a 9999 |
| k | 1.5, 2.0 o 2.5 |
| beta | 0.4, 0.8 o 1.2 |
| Ruido, desviación estándar | 0.03, 0.08 o 0.15 N |
| Temperatura de operación | tau=-0.5, 0 o 0.5, equivalentes a 20, 25 o 30 °C |

Conserva estos parámetros durante la comparación. La fórmula del simulador sirve para generar datos y para la comprobación final; no uses sus coeficientes como solución del ajuste.

Reserva **25 % para prueba**, con `random_state=2026`, usando la partición suministrada. Entrena **LinearRegression, Ridge y Lasso**, todos sobre la misma base polinómica de **grado 3** con interacciones. El grado queda fijo: no se exige buscar grados adicionales.

El pipeline suministrado es `PolynomialFeatures(degree=3, include_bias=False) → StandardScaler → estimador(fit_intercept=True)`. Usa **tres pliegues** de validación cruzada, iguales para las tres familias, dentro del conjunto de entrenamiento. Las transformaciones se ajustan dentro de cada pliegue; no sobre todos los datos antes de validar. [Pipelines](https://scikit-learn.org/stable/modules/compose.html), [fuga de información](https://scikit-learn.org/stable/common_pitfalls.html).

Las búsquedas ya configuradas usan:

- Ridge: `alpha = [0.0001, 0.01, 0.1, 1, 10]`.
- Lasso: `alpha = [0.0001, 0.001, 0.003, 0.01, 0.1]`.
- OLS: sin penalización que seleccionar.

El criterio es RMSE medio de validación (`neg_root_mean_squared_error`; cambia el signo al informar). Para Lasso se usan `max_iter=50000` y `tol=1e-6`. Registra y atiende advertencias de convergencia; no las ocultes. Elige la familia operativa **solo por validación**, antes de mirar la prueba.

**Evidencia:** una tabla de tres filas con familia, alpha, RMSE medio de validación y número de coeficientes no nulos (sin intercepto, umbral `1e-8`). Explica por qué un modelo polinómico puede seguir siendo lineal en sus parámetros. No se exige que Ridge o Lasso ganen.

## 2. Del estimador al sistema lineal

Reproduce el mejor Ridge sobre los datos de entrenamiento, aunque no sea la familia elegida para operar. Usa la misma expansión, escalador y alpha. Si Z es la matriz estandarizada, define `A=[1,Z]`, `D=diag(0,1,...,1)` y resuelve:

`(A.T @ A + alpha*D)c = A.T @ y`.

Puedes reutilizar tu solucionador del viernes o usar `numpy.linalg.solve`. Aquí se evalúa la formulación y su comprobación, no una tercera implementación del mismo algoritmo. El intercepto no se penaliza. No formes la inversa.

Reporta el máximo residuo del sistema y la diferencia máxima entre tus predicciones y las de Ridge en entrenamiento; explica diferencias mayores de `1e-6 N`. Compara además `cond(A.T@A)` y `cond(A.T@A+alpha*D)`, usando `numpy.linalg.cond`. No es obligatorio estudiar QR, SVD ni reconstruir esos algoritmos.

Ridge minimiza `||y-Ac||² + alpha||c_sin_intercepto||²`; Lasso utiliza `||y-Ac||²/(2n) + alpha||c_sin_intercepto||_1`. Explica la diferencia entre penalizaciones y por qué Lasso no se obtiene agregando una constante a la diagonal. El mismo alpha no tiene una intensidad numéricamente equivalente en ambas convenciones. [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html), [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html).

**Evidencia:** ecuación construida, comparación numérica y explicación breve de regularización e intercepto.

## 3. Una decisión física con el modelo

Congela la familia elegida por validación. A la temperatura seleccionada, define `m(z)=F_predicha(z,tau_operacion)` y busca `m(z)-1=0` en `[0,0.9]` con **tu bisección del curso o del viernes**. Solo se requiere un buscador.

Exige residuo `≤1e-7 N`, semianchura `≤1e-7` en z y máximo 100 iteraciones. Explora primero 101 puntos del intervalo para detectar cambios de signo o comportamientos incompatibles con una calibración creciente. Si hay ambigüedad o no hay raíz, explica el problema; no cambies de modelo después de consultar la prueba.

Estima la pendiente local por diferencias centrales con `h=1e-3` y `h=5e-4`. Compara ambos resultados y calcula la rigidez `m'(z_*)/L`, en N/m. Puedes usar las funciones del viernes; no es obligatorio derivar internamente el pipeline.

Para `delta_F=0.01 N`, estima `delta_x≈L*delta_F/abs(m'(z_*))`. Comprueba la predicción repitiendo la búsqueda para una fuerza de **1.01 N**. Informa posiciones en metros. Una pendiente cercana a cero es una limitación de la inversión, no una razón para ocultar el resultado.

**Evidencia:** tabla con posición, residuo, iteraciones, pendiente y desplazamiento estimado/observado; figura fuerza–posición con objetivo y solución.

## 4. Comprobación final y recomendación

Una vez fijadas todas las decisiones, evalúa los tres candidatos en la prueba reservada **una sola vez**. Añade a la primera tabla el RMSE de prueba en N. Mantén la elección operativa tomada por validación, incluso si el orden cambia en prueba. Compara también con predecir siempre la media de la fuerza del conjunto de entrenamiento.

Consulta al final la fuerza sin ruido del simulador y calcula su posición para 1 N a la misma temperatura, reutilizando la bisección. Compara con la posición predicha y distingue error del modelo, error de búsqueda y ruido de las observaciones. Esta consulta no permite volver a seleccionar ni reajustar el modelo.

Entrega un notebook o script ejecutable con parámetros, versiones e índices de partición. Reutiliza el generador; **no se exige adjuntar además un CSV ni un informe separado**. Incluye las dos tablas anteriores, los diagnósticos algebraicos, la figura de fuerza y una conclusión de **200 a 300 palabras** con la recomendación y sus límites.

Dentro de la conclusión explica con tus palabras tres ideas de consulta: escalamiento/fuga de información, penalizaciones Ridge/Lasso y condicionamiento frente a capacidad predictiva. Cita las lecturas utilizadas. No hay una revisión bibliográfica adicional.

## Rúbrica

La valoración R está sobre 100 y el aporte es **P=3R/100**. Se evalúa únicamente el núcleo obligatorio.

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Datos y reproducibilidad · 10 | **10:** parámetros, partición y ejecución reproducibles | **7:** una omisión menor | **3:** reconstrucción incompleta | **0:** no verificable |
| Comparación y validación · 30 | **30:** tres familias, mismos pliegues, escalamiento correcto, selección por CV y prueba al final | **21:** comparación válida con un diagnóstico pendiente | **9:** comparación incompleta o sin validación verificable | **0:** sin comparación válida o usa prueba para entrenar/seleccionar |
| Álgebra y regularización · 25 | **25:** reproduce Ridge, intercepto correcto, residuos y condición interpretados | **17:** formulación correcta con una comprobación pendiente | **7:** sistema reconocible sin contraste suficiente | **0:** penalización incorrecta o sin conexión algebraica |
| Decisión numérica · 25 | **25:** bisección controlada, pendiente, perturbación y referencia final con unidades | **17:** decisión válida con una comprobación pendiente | **7:** una posición sin validación suficiente | **0:** no desarrolla la decisión |
| Interpretación y consulta · 10 | **10:** recomendación sustentada, tres conceptos aplicados y fuentes | **7:** interpretación coherente con una omisión | **3:** describe herramientas sin conectar resultados | **0:** sin interpretación propia |

No se penaliza detectar correctamente que el modelo no permite una decisión confiable. Las ampliaciones no son necesarias para 100/100.

La distribución es **miércoles 1 + viernes 1 + opcional 3 = 5.0**. Las tres entregas con valoración completa permiten la exoneración. Consulta la [regla de evaluación](../../assessments/README.md#segundo-parcial-talleres-y-exoneración) para los aportes parciales y el examen.

## Ampliaciones de consulta, no evaluadas

Quien quiera profundizar puede variar el grado, estudiar curvas de regularización, hacer bootstrap, comparar ecuaciones normales con `lstsq`, analizar el sistema Ridge con Jacobi/potencias o formular una inversión en dos variables con Newton/Broyden. No se exige ninguna de estas actividades y no aumentan la nota.

## Lecturas de partida

- [Modelos lineales y regularización](https://scikit-learn.org/stable/modules/linear_model.html).
- [Pipelines](https://scikit-learn.org/stable/modules/compose.html) y [errores frecuentes al preparar datos](https://scikit-learn.org/stable/common_pitfalls.html).
- [Validación cruzada](https://scikit-learn.org/stable/modules/cross_validation.html).
- [Número de condición con NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html).

Retoma también los apartados de sistemas lineales, ceros, diferenciación y mínimos cuadrados de los apuntes y del libro guía.
