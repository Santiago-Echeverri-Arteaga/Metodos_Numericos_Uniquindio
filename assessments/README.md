# Sistema de evaluación 2026-2

La concertación académica firmada el 2 de septiembre de 2026 establece tres parciales,
todos realizados mediante Aulas Virtuales.

| Corte | Fecha concertada | Unidades principales | Peso |
|---|---:|---|---:|
| Parcial 1 | 30/09/2026 | 1. Error numérico y 2. Derivación | 33,4 % |
| Parcial 2 | 28/10/2026 | 3. Álgebra lineal y 4. Ceros/minimización | 33,3 % |
| Parcial 3 | 20/11/2026 | 5. Aproximación, 6. Integración y 7. Ecuaciones diferenciales | 33,3 % |
| **Total** | | | **100 %** |

Las fechas pueden cambiar únicamente por directrices de la Universidad y cualquier
modificación debe comunicarse por los canales institucionales.

## Estructura recomendada de cada parcial

Para conservar una evaluación significativa sin multiplicar entregas ni trabajo de
calificación, cada parcial puede combinar preguntas de calificación automática con dos
respuestas de revisión manual.

| Bloque | Evidencia | Calificación sugerida |
|---|---|---:|
| Conceptos, predicciones y selección de método | Reconoce supuestos, orden, estabilidad y método apropiado | 30 % automática |
| Trazado y lectura de código | Sigue iteraciones, identifica salidas y detecta defectos | 30 % automática |
| Análisis numérico breve | Explica error, residuo, sensibilidad o criterio de parada | 20 % manual |
| Caso de transferencia | Interpreta un caso nuevo y justifica una decisión | 20 % manual |

Esta distribución es una recomendación operativa, no una condición adicional del acta.
La estructura se aplica a los intentos de examen. La alternativa de talleres para el
segundo parcial se describe al final de este documento.

## Qué se evalúa en cada corte

### Parcial 1

- Fuentes de error, representación finita y cancelación.
- Propagación, condicionamiento y estabilidad.
- Diferencias finitas, tamaño de paso y extrapolación de Richardson.
- Diferenciación automática y lectura de implementaciones breves.

### Parcial 2

- Normas, residuo y condicionamiento de sistemas lineales.
- Eliminación, pivoteo, factorización y métodos iterativos.
- Problemas de valores propios.
- Bisección, punto fijo, Newton, secante, Ridder y minimización.
- Criterios de parada y diagnóstico de convergencia.

### Parcial 3

- Interpolación, elección de nodos, ajuste y análisis de residuos.
- Newton-Cotes, integración adaptativa, Gauss-Legendre y Monte Carlo.
- Problemas de valores iniciales, Euler, Runge-Kutta y estabilidad.
- Selección de métodos y validación de resultados en un contexto físico.

## Criterio de corrección para preguntas abiertas

Cada respuesta abierta se valora mediante cuatro marcas sencillas:

- `M`: comprende y selecciona correctamente el método.
- `E`: identifica y analiza el error relevante.
- `V`: propone o interpreta una validación apropiada.
- `I`: comunica una conclusión matemática o física sustentada.

Una respuesta completa obtiene las cuatro marcas. Este sistema permite retroalimentar
sin redactar comentarios individuales extensos.

## Límites del sistema

- No se califican ejercicios del libro, talleres de práctica ni avances. Las actividades con aporte al segundo parcial se especifican abajo.
- Los códigos del libro son material de consulta, no bancos de respuestas.
- Los talleres de las páginas HTML son práctica de apoyo y no generan una cuarta nota.
- La duración, disponibilidad y reglas específicas de cada intento se publican en Aulas
  Virtuales.

## Segundo parcial: talleres y exoneración

El segundo parcial permite integrar el trabajo de clase y un proyecto opcional. Su
peso en la nota del curso sigue siendo **33,3 %**; la escala de este parcial es de 0 a 5.

| Actividad | Valoración R sobre 100 | Aporte máximo |
| --- | --- | ---: |
| [Laboratorio computacional del miércoles 7/10](../teaching-assets/talleres_2026_10/miercoles_ejercicios.md) | R_m | 1 punto |
| [Proyecto del viernes 9/10, variante B](../teaching-assets/taller_integrador_aproximacion.md) | R_v | 1 punto |
| [Proyecto opcional de regresión](../teaching-assets/talleres_2026_10/proyecto_opcional_regresion.md) | R_p | 3 puntos |
| **Total por talleres** | | **5 puntos** |

Los aportes son `M=R_m/100`, `V=R_v/100` y `P=3R_p/100`.
**Los tres talleres con valoración completa (100/100 cada uno) dan 5.0 y
exoneración del examen del segundo parcial.** La variante A del viernes es
práctica y no reemplaza la entrega evaluable de la variante B.

Quien no realiza el proyecto opcional presenta el examen del segundo parcial,
que aporta hasta **3 puntos**: si E es su nota sobre 5, el aporte es `0.6 E`.
La nota resulta `M + V + 0.6 E`.

Si se presenta el proyecto opcional con valoración parcial y no se alcanza la
exoneración, se presenta el examen. Se conserva el mejor aporte dentro del bloque
de tres puntos: `nota = M + V + max(P, 0.6 E)`. No se suman proyecto y examen
como bloques independientes, ni se pierden los puntos ya obtenidos del proyecto.
Por ejemplo, M=0.8, V=0.9, P=2.1 y E=4.0 producen `0.8+0.9+2.4=4.1`.
El máximo sigue siendo 5.0.

Las entregas deben ser ejecutables y corresponder al trabajo individual. Las
rúbricas de cada enunciado determinan la valoración; completar archivos sin
verificar resultados no equivale a obtener la totalidad de los puntos.

Las ampliaciones de consulta no son necesarias para obtener 100/100. El miércoles
se valoran el experimento 1 y dos electivos; el viernes y el opcional se valoran
únicamente según su núcleo obligatorio. Se permite reutilizar código de una
entrega en las siguientes, indicando su procedencia.
