# Métodos Numéricos para Física

## Presentación del espacio académico

Los métodos numéricos permiten construir respuestas aproximadas cuando un problema físico no tiene una solución analítica accesible, cuando los datos solo están disponibles en forma discreta o cuando la complejidad del modelo hace necesario el cálculo computacional. El propósito del curso no es coleccionar fórmulas: es aprender a seleccionar un método, implementarlo, estimar su error, reconocer cuándo puede fallar y justificar si el resultado es físicamente razonable.

El curso recorre una secuencia que va desde la aritmética finita y el análisis de errores hasta la solución aproximada de ecuaciones diferenciales. Python será el medio de experimentación: permitirá comparar métodos, observar convergencia, estudiar estabilidad y contrastar resultados con soluciones conocidas o con implementaciones de referencia.

> **Documentos del curso:** este recurso acompaña las notas de clase de Métodos Numéricos, el acta de concertación académica 2026-2 y el libro de Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, Cambridge University Press, 2023. Los PDF deben publicarse junto con estos materiales en Moodle.

## Identificación

| Campo | Información |
| --- | --- |
| Facultad | Ciencias Básicas y Tecnologías |
| Programa | Física |
| Espacio académico | Métodos Numéricos |
| Grupo | 01 |
| Jornada | Diurna |
| Período académico | 2026-2 |
| Profesor | Santiago Echeverri Arteaga |
| Correo institucional | [secheverri@uniquindio.edu.co](mailto:secheverri@uniquindio.edu.co) |
| Herramienta principal | Python y su ecosistema científico |
| Medio principal del curso | Moodle / Aulas Virtuales |

## Propósito formativo

Al finalizar el curso, el estudiante deberá poder formular un problema numérico a partir de una situación física, identificar sus fuentes de error, escoger un algoritmo adecuado, implementarlo de manera clara, comprobar su convergencia y comunicar las limitaciones de la respuesta obtenida.

Una solución numérica completa debe responder, como mínimo, cinco preguntas:

1. ¿Qué problema matemático representa la situación física?
2. ¿Qué información de entrada se conoce y con qué precisión?
3. ¿Qué método se emplea y bajo qué condiciones funciona?
4. ¿Cómo se estima o verifica el error?
5. ¿Qué evidencia permite confiar en el resultado?

## Resultados de aprendizaje

| N.º | Al finalizar el curso, el estudiante podrá… | Evidencia esperada |
| --- | --- | --- |
| 1 | Diferenciar error de medición, redondeo, truncamiento y propagación | Cálculo de errores y explicación de su origen |
| 2 | Analizar estabilidad, convergencia y condicionamiento | Comparación cuantitativa entre métodos o formulaciones |
| 3 | Aproximar derivadas y seleccionar un tamaño de paso justificable | Tabla o gráfica de error frente al paso |
| 4 | Resolver sistemas lineales y problemas de valores propios | Implementación, residuo y análisis del condicionamiento |
| 5 | Localizar ceros y mínimos de funciones escalares o sistemas | Criterios de parada, historial de iteraciones y residuo |
| 6 | Interpolar datos y construir modelos por mínimos cuadrados | Validación sobre datos no usados o análisis de residuos |
| 7 | Aproximar integrales mediante reglas deterministas y Monte Carlo | Estudio de convergencia y estimación de incertidumbre |
| 8 | Resolver problemas de valores iniciales y reconocer problemas de frontera | Comparación con solución exacta, refinamiento o invariantes |
| 9 | Diseñar experimentos computacionales reproducibles | Código organizado, parámetros explícitos y resultados verificables |
| 10 | Interpretar numéricamente un resultado dentro de su contexto físico | Unidades, órdenes de magnitud, límites y discusión |

## Organización por unidades

| Unidad | Núcleo temático | Métodos y productos principales | Texto de referencia |
| --- | --- | --- | --- |
| 1 | Error numérico y representación | Error absoluto/relativo, propagación, punto flotante, cancelación, estabilidad | Gezerlis, cap. 2 |
| 2 | Derivación numérica y automática | Diferencias finitas, elección de paso, extrapolación, números duales | Gezerlis, cap. 3 |
| 3 | Álgebra lineal numérica | Normas, condicionamiento, sistemas triangulares, eliminación, métodos iterativos, valores propios | Gezerlis, cap. 4 |
| 4 | Ceros y minimización | Bisección, punto fijo, Newton, secante, Ridder, sistemas no lineales y búsqueda de mínimos | Gezerlis, cap. 5 |
| 5 | Aproximación, interpolación y ajuste | Lagrange, nodos de Chebyshev, splines, mínimos cuadrados y residuos | Gezerlis, cap. 6 |
| 6 | Integración numérica | Newton-Cotes, trapecio, Simpson, adaptación, Gauss-Legendre y Monte Carlo | Gezerlis, cap. 7 |
| 7 | Ecuaciones diferenciales | Euler, Runge-Kutta, sistemas, estabilidad, frontera y problemas de valores propios | Gezerlis, cap. 8 |

## Ruta sugerida por cortes

La secuencia concreta puede ajustarse según las directrices institucionales y el avance del grupo. La siguiente tabla organiza los contenidos de manera coherente con las tres evaluaciones concertadas.

| Corte | Unidades principales | Trabajo de preparación | Evaluación |
| --- | --- | --- | --- |
| Primero | 1. Error numérico y 2. Derivación | Ejercicios de propagación, experimentos con punto flotante, diferencias finitas y extrapolación | Parcial 1 — 30/09/2026 |
| Segundo | 3. Álgebra lineal y 4. Ceros/minimización | Sistemas lineales, residuos, condicionamiento, iteraciones de raíces y búsqueda de mínimos | Parcial 2 — 28/10/2026 |
| Tercero | 5. Aproximación, 6. Integración y 7. Ecuaciones diferenciales | Interpolación, ajuste, cuadratura, Monte Carlo, problemas de valores iniciales y sistemas | Parcial 3 — 20/11/2026 |

## Plan de evaluación concertado

| Fecha | Estrategia evaluativa | Porcentaje |
| --- | --- | --- |
| 30/09/2026 | Parcial 1 | 33,4 % |
| 28/10/2026 | Parcial 2 | 33,3 % |
| 20/11/2026 | Parcial 3 | 33,3 % |
|   | **Total** | **100 %** |

Los parciales se realizarán mediante Aulas Virtuales. Las fechas y condiciones pueden cambiar si la Universidad emite nuevas directrices. Cualquier modificación deberá comunicarse por los canales institucionales.

## Estructura recomendada de cada parcial

| Tipo de desempeño | Qué debe demostrar el estudiante |
| --- | --- |
| Comprensión conceptual | Explicar por qué funciona un método y reconocer sus supuestos |
| Trazado de algoritmo | Seguir iteraciones, estimar el siguiente valor y detectar errores |
| Implementación | Completar o escribir una función corta con una interfaz definida |
| Análisis de error | Estimar orden, residuo, error absoluto/relativo o sensibilidad |
| Decisión metodológica | Elegir entre dos métodos y justificar el criterio |
| Interpretación física | Revisar unidades, signos, límites y plausibilidad del resultado |

## Metodología de trabajo

Cada tema se estudiará mediante un ciclo de cinco momentos:

1. **Problema:** se plantea una situación física o matemática que no se resuelve de forma directa.
2. **Modelo:** se identifican variables, unidades, ecuaciones, datos, condiciones y cantidad buscada.
3. **Método:** se deriva o explica el algoritmo y se anticipa su error.
4. **Experimento computacional:** se implementa, prueba y compara el método en Python.
5. **Validación:** se usa una solución exacta, un residuo, una ley de conservación, refinamiento de malla o una biblioteca confiable.

| Momento de una clase | Duración orientativa | Producto verificable |
| --- | --- | --- |
| Activación y predicción | 10–15 min | Hipótesis o estimación previa |
| Desarrollo conceptual | 25–35 min | Derivación, esquema o tabla de decisión |
| Implementación guiada | 30–45 min | Función pequeña y casos de prueba |
| Experimentación | 20–30 min | Tabla o gráfica de convergencia |
| Cierre | 10–15 min | Conclusión sustentada por evidencia |

## Protocolo para resolver un problema numérico

| Etapa | Pregunta de control | Evidencia mínima |
| --- | --- | --- |
| 1. Formular | ¿Cuál es la entrada, la salida y la ecuación? | Variables, unidades y dominio |
| 2. Anticipar | ¿Qué orden de magnitud y signo se esperan? | Estimación manual |
| 3. Seleccionar | ¿Qué condiciones exige el método? | Justificación de la elección |
| 4. Implementar | ¿La función tiene entradas y salidas claras? | Código legible y casos simples |
| 5. Verificar | ¿Qué residuo, error o invariante se puede calcular? | Métrica cuantitativa |
| 6. Refinar | ¿Qué cambia al reducir el paso o aumentar iteraciones? | Estudio de convergencia |
| 7. Comunicar | ¿Qué tan confiable es la respuesta? | Resultado con unidades y limitaciones |

## Requisitos mínimos del código

- Evitar valores físicos ocultos dentro de las funciones.
- Documentar entradas, salidas, unidades y restricciones.
- Separar cálculo, visualización y lectura de datos.
- Incluir criterios de parada y un número máximo de iteraciones.
- Comprobar valores no finitos (`NaN`, `inf`) cuando puedan aparecer.
- Conservar el historial de iteraciones cuando sea útil para diagnosticar.
- Comparar contra un caso conocido antes de confiar en un caso nuevo.
- Explicar por qué una gráfica o tabla demuestra lo que se afirma.

## Plantilla de una experiencia computacional

```python
def metodo(datos, tolerancia=1e-8, max_iter=100):
    """Devuelve aproximación, diagnóstico e historial."""
    # 1. Validar entradas
    # 2. Construir aproximación inicial
    # 3. Iterar y registrar una métrica de error o residuo
    # 4. Detener por convergencia o por límite de iteraciones
    # 5. Devolver información suficiente para verificar
    raise NotImplementedError
```

La interfaz anterior no es una receta universal. Su función es recordar que un método científico debe devolver algo más que un número: también debe informar si convergió, con qué criterio y bajo qué parámetros.

## Estrategias de validación

| Estrategia | Aplicación típica | Pregunta clave |
| --- | --- | --- |
| Solución exacta | Problemas de prueba | ¿El error disminuye como predice la teoría? |
| Residuo | Sistemas, raíces y ecuaciones diferenciales | ¿La aproximación satisface la ecuación? |
| Refinamiento | Derivación, integración y EDO | ¿El resultado se estabiliza al reducir el paso? |
| Método independiente | Cualquier unidad | ¿Dos métodos distintos coinciden dentro de la tolerancia? |
| Invariante físico | Dinámica y sistemas conservativos | ¿Se conserva energía, norma, masa u otra cantidad? |
| Orden de magnitud | Todo problema físico | ¿El valor es plausible antes de mirar decimales? |

## Uso responsable de herramientas computacionales

Las bibliotecas científicas son referencias útiles, pero no reemplazan la comprensión. Cuando se utilice una función de NumPy, SciPy u otra herramienta, el estudiante debe identificar qué problema resuelve, qué parámetros controlan el método y cómo interpretar su resultado.

Si una actividad autoriza inteligencia artificial, el código o explicación obtenidos deben revisarse mediante pruebas independientes. Entregar una respuesta que no pueda explicarse, modificarse o validar impide demostrar aprendizaje.

## Bibliografía de trabajo

| Recurso | Uso dentro del curso |
| --- | --- |
| Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos* | Secuencia de explicaciones, derivaciones y ejemplos tratados en clase |
| Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª ed., CUP, 2023 | Texto técnico principal, proyectos físicos y problemas de profundización |
| Acta de concertación académica, Métodos Numéricos, 2026-2 | Fechas, porcentajes y condiciones operativas de evaluación |
| Documentación oficial de Python, NumPy, SciPy y Matplotlib | Consulta de interfaces y comportamiento de las bibliotecas |

## Recomendaciones para estudiar

1. Resuelva primero un caso pequeño a mano.
2. Prediga el signo y el orden de magnitud antes de ejecutar.
3. Dibuje el algoritmo o escriba sus pasos en lenguaje natural.
4. Cambie un parámetro por vez y registre el efecto.
5. No confunda que el programa termine con que la respuesta sea correcta.
6. Compare error, residuo y cambio entre iteraciones: no son la misma cantidad.
7. Conserve ejemplos que hagan fallar el método; son parte del aprendizaje.
8. Estudie con preguntas de decisión: “¿qué método usaría y por qué?”.

---

**Documento de referencia institucional:** Acta de concertación académica del 2 de septiembre de 2026. **Texto técnico:** Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, Cambridge University Press, 2023.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
