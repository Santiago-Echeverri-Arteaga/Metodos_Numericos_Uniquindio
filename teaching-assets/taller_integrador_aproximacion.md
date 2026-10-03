# Viernes: ¿dónde queda el equilibrio de un resorte no lineal?

**9 de octubre de 2026 · Sesión de dos horas · Trabajo individual**

En este proyecto aplicaremos los temas vistos en clase: aritmética y error, diferencias finitas y Richardson, sistemas lineales con pivoteo, interpolación polinómica, ecuaciones normales, búsqueda de ceros y minimización. No requiere contenidos posteriores a aproximación.

## Una decisión, un proyecto

Debes recomendar la posición de montaje de un resorte no lineal sometido a una fuerza constante. La recomendación debe incluir una estimación del error y evidencia de que la posición corresponde a un equilibrio estable. El laboratorio acepta un error de posición de **0.015 L**. Si la aproximación no cumple esa especificación, concluye que es insuficiente y explica qué cambiarías.

La energía se expresa como `U(x) = E0 u(z)`, donde `z = x/L` y

`u(z) = sqrt(1 + alpha*z²) - 1 - q*z`, para `-1 ≤ z ≤ 1`.

Aquí `L = 0.02 m`, `E0 = 0.10 J` y la fuerza aplicada es `F = q E0/L`. La parte elástica es convexa; el término `-q*z` representa el trabajo de la fuerza. Es un modelo idealizado: el proyecto trata su aproximación numérica, no la caracterización experimental de un resorte real.

El banco de prueba permite consultar esta función, pero **la posición debe calcularse a partir de una aproximación construida con nueve muestras**. Las consultas adicionales sirven para validar; no se agregan al ajuste. Resolver únicamente el modelo exacto no cumple el encargo.

## Elige tu diseño dentro de estos límites

Escoge `alpha` entre **1, 4 y 9**, y `q` entre **0.20, 0.30 y 0.40**. Elige también una distribución de nueve muestras:

- Uniforme: `z_i = -1 + 2i/8`.
- Chebyshev con extremos: `z_i = -cos(i*pi/8)`.

En ambos casos `i = 0,...,8`. Hay 18 configuraciones posibles. Registra tu elección antes de calcular. Puedes compartir configuración con otra persona: se evalúan tu implementación, tus comprobaciones y tu decisión.

Usa la expresión equivalente `u(z) = alpha*z²/(sqrt(1+alpha*z²)+1) - q*z` para generar los datos. Explica por qué protege el término elástico cerca de cero. La [plantilla](talleres_2026_10/viernes_base.py) entrega muestras, malla de comprobación y utilidades elementales; funciona con Python estándar.

## Dos variantes

| | A · Actividad de clase | B · Trabajo evaluable |
| --- | --- | --- |
| Trabajo científico | El recorrido común descrito abajo | El mismo recorrido, con implementación y controles adicionales delimitados |
| Herramientas | NumPy, SciPy y Matplotlib permitidos | Python y biblioteca estándar; sin paquetes externos para calcular |
| Métodos lineales | `solve` sobre Vandermonde o ecuaciones normales; no sustituir estas últimas por `lstsq`, QR o SVD | Eliminación con pivoteo parcial y sustitución hacia atrás propias |
| Interpolación | Base monómica, Lagrange o fórmula baricéntrica | Rutina baricéntrica suministrada, cuyo resultado debes comprobar |
| Evidencia adicional | Interpretación de las salidas de biblioteca | Código visible y dos pruebas de control |
| Entrega | Notebook o script con conclusión y tablas; gráficos opcionales | Script con conclusión y tablas; sin gráficos obligatorios |
| Valor | Práctica sin aporte al parcial | Hasta **1.0 punto del segundo parcial** |

**Aporte al segundo parcial:** la variante B aporta `V=R_v/100`, hasta 1 punto. El taller computacional del miércoles aporta otro punto y el proyecto opcional de regresión hasta tres. Con valoración completa en los tres se obtiene **5.0 y exoneración del examen del segundo parcial**. La variante A no acredita el punto del viernes. Consulta la [distribución completa](../assessments/README.md#segundo-parcial-talleres-y-exoneración).

## El recorrido común

### De nueve muestras a una representación de la energía

Construye un interpolante de grado a lo sumo ocho con la rutina suministrada y un ajuste `P4` de grado cuatro. Forma explícitamente sus ecuaciones normales:

`M_jk = sum(z_i**(j+k))`, `b_j = sum(u_i*z_i**j)`, `M c = b`.

Los índices van de cero al grado. En A puedes usar operaciones matriciales; en B usa sumas y listas. Muestra la matriz, el vector y el máximo residuo del sistema `max(abs(Mc-b))` del ajuste P4. No calcules la inversa para resolver: distingue el residuo del sistema del error de aproximar la energía.

Compara las dos representaciones en los **40 puntos nuevos** `z_j = -1 + (j+0.5)/20`, `j = 0,...,39`, mediante el máximo error absoluto respecto a `u`. Verifica además que el interpolante reproduce los nueve nodos. Usa los mismos puntos de comprobación para las dos representaciones y explica por qué verificar solo los nodos no basta.

La representación operativa será **P4**, incluso si el interpolante tiene menor error: interesa comprobar si cinco coeficientes permiten cumplir la especificación de posición. Explica el costo de esa elección. No se exige que un método gane siempre.

### De la energía al equilibrio estable

El equilibrio satisface `P4'(z_*) = 0`. Obtén la primera derivada mediante diferencias centrales y Richardson:

`D_h(z) = [P4(z+h)-P4(z-h)]/(2h)`, `R_h(z) = [4D_(h/2)(z)-D_h(z)]/3`.

Usa `h = 0.01`. Encuentra el cero de `R_h` por **bisección en [0, 0.6]**, previa comprobación del cambio de signo. Exige semianchura de intervalo `≤ 1e-7`, residuo `abs(R_h) ≤ 1e-7` y máximo 100 iteraciones. Informa si ambas condiciones se alcanzan. Una raíz exacta permite cerrar el intervalo en ese punto.

Comprueba la derivada extrapolada evaluando también la derivada obtenida de los coeficientes de P4 en la raíz hallada. Reporta posición, residuo, intervalo final e iteraciones de la bisección. No es obligatorio implementar un segundo buscador: la comparación entre ambas formas de derivar sirve como control independiente del cálculo de la derivada.

Calcula la segunda derivada central de `P4` en el equilibrio con `h=0.01` y `0.005`; verifica su signo y compara con la obtenida de los coeficientes. La rigidez efectiva es `k_ef = (E0/L²) P4''(z_*)`, en N/m. Para justificar la unicidad o el intervalo de minimización, verifica el signo de `P4''` en `[0,0.6]`: es cuadrática, así que basta revisar extremos y vértice si está dentro.

### Del resultado numérico a una recomendación

Calcula una referencia independiente resolviendo

`alpha*z/sqrt(1+alpha*z²) - q = 0`

con bisección en `[0,0.6]`, tolerancias `1e-10` en semianchura y residuo, y máximo 100 iteraciones. Es una referencia del modelo ideal, no un dato de entrenamiento. Compara `L*abs(z_* - z_ref)` con `0.015 L`: una búsqueda precisa del cero de P4 no elimina el error de aproximación de P4.

## Exigencia adicional de B

Entrega y explica **dos rutinas propias: eliminación con pivoteo parcial y bisección con control de convergencia**. Puedes reutilizar tus implementaciones de clase o del miércoles, sin volver a programarlas. La plantilla proporciona interpolación baricéntrica, generación de datos, ecuaciones normales, evaluación polinómica y diferencias. B usa Python estándar; no exige implementar el interpolante desde cero.

Incluye estas dos pruebas y su resultado:

- Resolver `[[0,2],[1,3]] c = [4,7]` debe dar `c=[1,2]` e intercambiar filas. Detecta y comunica un pivote numéricamente nulo.
- Bisección para `t²-2=0` en `[1,2]` debe cumplir las tolerancias y rechazar `[2,3]`. Agotar iteraciones debe informarse, no presentarse como éxito.

La dificultad evaluable está en conectar ambos métodos con el problema y comprobar sus resultados. No se exige una biblioteca completa ni repetir el banco de pruebas del miércoles.

## Ampliaciones de consulta, sin efecto en la nota

Puedes añadir el ajuste P2, comparar un segundo buscador (Newton, secante, Ridder o sección áurea), experimentar con Kahan o propagar `delta_q=0.001` mediante `delta_z≈delta_q/P4''(z_*)` y comprobar el resultado con una nueva búsqueda. Ninguna ampliación es necesaria para obtener 100/100 o la exoneración.

## Entrega y rúbrica

Entrega un notebook o script ejecutable y una conclusión de **150 a 250 palabras** dentro del archivo o en texto adjunto. Incluye una tabla de errores de aproximación, una de resultados de equilibrio y otra de rigidez. Matrices y pruebas pueden aparecer como salida de texto. La conclusión debe indicar `alpha`, `q`, nodos, posición en metros, rigidez en N/m, cumplimiento o incumplimiento de la especificación y limitación principal.

Cada fila recibe uno de los cuatro puntajes indicados. En A se usa para retroalimentación; en B determina el aporte. Todas las configuraciones tienen el mismo valor. La rúbrica evalúa únicamente el núcleo obligatorio.

| Criterio | Completo | Parcial | Inicial | Ausente o inválido |
| --- | --- | --- | --- | --- |
| Representación y aproximación · 20 | **20:** interpolante y P4 correctos; ecuaciones normales visibles; prueba en nodos y errores en 40 puntos nuevos | **14:** ambas representaciones funcionan, falta una comprobación | **6:** una representación válida o validación solo en nodos | **0:** sin aproximación evaluable |
| Solución lineal · 20 | **20:** resuelve el sistema y reporta residuo; en B pivoteo propio y prueba de intercambio correctos | **14:** coeficientes válidos, falta un diagnóstico o prueba | **6:** procedimiento reconocible con fallo en el ajuste | **0:** sin solución válida; en B sustituye la rutina propia por un solucionador externo |
| Equilibrio y convergencia · 20 | **20:** bisección con hipótesis, tolerancias, intervalo y estado claros; en B prueba de rechazo correcta | **14:** raíz válida, falta un control | **6:** propuesta de raíz sin acreditar convergencia | **0:** sin equilibrio; en B no presenta bisección propia |
| Derivación y estabilidad · 15 | **15:** contrasta Richardson y segunda derivada con las derivadas de P4; verifica convexidad y rigidez | **10:** estabilidad justificada, falta una comparación | **4:** derivada sin validar o signo físico incorrecto | **0:** no determina estabilidad |
| Error y precisión de montaje · 15 | **15:** contrasta con la referencia, verifica la especificación y explica racionalización y error de aproximación frente al de búsqueda | **10:** análisis correcto con una comprobación ausente | **4:** diferencias numéricas sin interpretación | **0:** afirma precisión sin evidencia |
| Reproducibilidad y decisión · 10 | **10:** ejecución completa, unidades claras y recomendación sustentada | **7:** una omisión menor | **3:** ejecución incompleta o conclusión genérica | **0:** no hay entrega verificable |

No se penaliza un diseño que incumpla la especificación si se detecta y explica correctamente. Usar el interpolador suministrado está permitido también en B; no reduce la nota.

## Condiciones de aplicación

La sesión presupone Python listo, plantilla disponible y consulta o reutilización del código propio trabajado en clase. B no presupone escribir todos los métodos desde cero. No se asignan tiempos por etapa.

El proyecto articula los temas vistos en clase. El [taller del miércoles](talleres_2026_10/miercoles_ejercicios.md) prepara el manejo y diagnóstico de los métodos; el viernes exige conectarlos en una decisión física. No se modifica el calendario general de parciales.
