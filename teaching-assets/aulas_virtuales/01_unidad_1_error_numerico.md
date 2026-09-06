# Unidad 1. Error numérico y representación finita

## Sentido de la unidad

Antes de aplicar cualquier algoritmo es necesario comprender qué significa “aproximar”. Un computador trabaja con representaciones finitas, los datos físicos tienen incertidumbre y los métodos reemplazan operaciones exactas por procedimientos aproximados. El resultado puede contener muchos decimales y, aun así, ser poco confiable.

Esta unidad desarrolla el vocabulario y las herramientas para describir el error, anticipar su propagación y reconocer operaciones numéricamente peligrosas. Es la base para interpretar todas las unidades posteriores.

> **Lectura orientadora:** notas de clase, sección inicial sobre error y propagación; Gezerlis, capítulo 2. Como repaso de Python y NumPy puede consultarse el capítulo 1.

## Resultados de aprendizaje

Al terminar la unidad, el estudiante podrá:

- distinguir valor exacto, valor aproximado, error y cota de error;
- calcular e interpretar errores absoluto y relativo;
- separar incertidumbre de entrada, error de redondeo y error del método;
- estimar la propagación de pequeñas perturbaciones;
- explicar overflow, underflow, precisión de máquina y cancelación catastrófica;
- diferenciar un problema mal condicionado de un algoritmo inestable;
- diseñar experimentos que revelen pérdida de precisión.

## Secuencia sugerida de clases

| Clase | Pregunta central | Conceptos | Evidencia breve |
| --- | --- | --- | --- |
| 1 | ¿Qué significa que un resultado sea aproximado? | Error absoluto, relativo, porcentaje y cotas | Cálculo manual con unidades |
| 2 | ¿Cómo afecta la incertidumbre de los datos al resultado? | Propagación univariable y multivariable | Comparación entre estimación lineal y perturbación directa |
| 3 | ¿Cómo representa números reales un computador? | Punto flotante, rango, precisión, `NaN`, `inf` | Experimentos con `float` y `numpy.finfo` |
| 4 | ¿Por qué expresiones equivalentes producen respuestas distintas? | Cancelación, orden de operaciones y estabilidad | Reformulación de una expresión problemática |
| 5 | ¿Cómo se audita un cálculo numérico? | Condicionamiento, estabilidad, residuo y validación | Informe corto de diagnóstico |

## 1. Tipos de error

Sea `x` el valor de referencia y `x_aprox` el valor calculado.

error absoluto = x_aprox - x

error relativo = (x_aprox - x) / x, siempre que x ≠ 0

Para comunicar magnitud suele usarse el valor absoluto del error. El signo, sin embargo, informa si la aproximación quedó por encima o por debajo del valor de referencia.

| Concepto | Qué describe | Unidad | Precaución |
| --- | --- | --- | --- |
| Error absoluto | Separación entre aproximación y referencia | La misma de la magnitud | No permite comparar escalas muy distintas |
| Error relativo | Error comparado con el tamaño del valor | Adimensional | No está definido si la referencia es cero |
| Error porcentual | Error relativo multiplicado por 100 | Porcentaje | Un porcentaje pequeño no garantiza relevancia física |
| Residuo | Qué tan bien la aproximación satisface la ecuación | Depende del problema | Un residuo pequeño no siempre implica error pequeño |
| Cota | Límite garantizado o estimado para el error | Depende de la métrica | Debe aclararse si es teórica o empírica |

### Ejemplo de escala

Un error absoluto de `0,01 m` puede ser excelente al medir una distancia de `100 m`, pero inaceptable al medir el espesor de una lámina de `0,02 m`. La interpretación depende de la escala, la finalidad y la incertidumbre de los datos.

## 2. Fuentes de error

| Fuente | Origen | Ejemplo | Cómo estudiarla |
| --- | --- | --- | --- |
| Medición | Resolución, calibración, ruido o procedimiento experimental | Longitud medida con regla milimetrada | Repeticiones, calibración e incertidumbre |
| Modelo | Simplificaciones de la representación física | Ignorar rozamiento | Comparar modelos o estimar términos despreciados |
| Truncamiento | Sustituir un proceso infinito por uno finito | Cortar una serie de Taylor | Analizar el término omitido y refinar |
| Discretización | Representar un continuo mediante puntos | Malla temporal en una EDO | Reducir el paso y estudiar convergencia |
| Redondeo | Representación finita de los números | `0.1 + 0.2` no coincide exactamente con `0.3` | Examinar escala, precisión y operaciones |
| Iteración | Detener un proceso antes de su límite | Parar Newton por tolerancia | Registrar residuo, cambio e iteraciones |

## 3. Propagación de pequeñas perturbaciones

Si `y = f(x)` y el dato cambia en una cantidad pequeña `Δx`, una aproximación de primer orden es:

Δy ≈ f′(x) Δx

Para varias variables `y = f(x₁, x₂, …, xₙ)`:

Δy ≈ Σ (∂f/∂xᵢ) Δxᵢ

Esta relación no distingue por sí sola entre una cota máxima y una incertidumbre estadística. Antes de combinar contribuciones debe aclararse qué significa cada `Δxᵢ` y si existen correlaciones.

### Actividad guiada

Para la energía cinética `K = m v² / 2`, estime el efecto de pequeñas variaciones en `m` y `v`. Después compare la aproximación lineal con una evaluación directa usando los valores perturbados. Determine cuál entrada domina la sensibilidad y explique por qué.

## 4. Punto flotante

Un número de punto flotante se almacena mediante signo, exponente y significando. La representación permite cubrir escalas muy grandes, pero solo conserva una cantidad finita de dígitos significativos.

| Fenómeno | Descripción | Síntoma habitual |
| --- | --- | --- |
| Redondeo | El real más cercano puede no ser representable | Igualdades decimales inesperadas |
| Overflow | La magnitud supera el máximo representable | `inf` o excepción según la operación |
| Underflow | La magnitud cae por debajo del rango normal | Resultado subnormal o cero |
| Pérdida de absorción | Una cantidad pequeña se suma a otra mucho mayor | La suma no cambia |
| Cancelación | Se restan números cercanos | Pérdida drástica de cifras significativas |

```python
import math
import numpy as np

info = np.finfo(float)
print("epsilon:", info.eps)
print("mínimo normal:", info.tiny)
print("máximo:", info.max)

print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3)
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-12))
```

### Comparación adecuada

Comparar flotantes solo con `==` puede ser incorrecto cuando los valores provienen de operaciones diferentes. Una prueba robusta suele combinar tolerancia relativa y absoluta:

|a - b| ≤ atol + rtol · max(|a|, |b|)

La tolerancia debe proceder del problema, no copiarse sin justificación.

## 5. Cancelación catastrófica

La cancelación aparece cuando se restan cantidades cercanas. Los dígitos comunes desaparecen y el error presente en los últimos dígitos pasa a dominar el resultado.

### Caso de estudio: serie de la exponencial

La serie `exp(x) = Σ xⁿ/n!` funciona bien para muchos valores positivos. Para un valor negativo de gran magnitud, los términos alternan, alcanzan magnitudes enormes y luego se cancelan para producir un número pequeño. La serie es matemáticamente correcta, pero evaluarla de esa manera puede ser numéricamente inestable.

Una reformulación útil es calcular `exp(-a)` como `1/exp(a)` cuando `a > 0`. La nueva expresión evita construir una respuesta diminuta mediante la resta de términos enormes.

```python
from math import exp

x = -20.0
estable = 1.0 / exp(-x)
referencia = exp(x)

print(estable)
print(referencia)
print(abs(estable - referencia))
```

La lección no es que toda serie sea mala, sino que una misma identidad matemática puede admitir implementaciones con comportamientos numéricos muy diferentes.

## 6. Suma compensada

Cuando se suman muchos términos de escalas diferentes, parte de las contribuciones pequeñas puede perderse. La suma compensada conserva una variable adicional para recuperar parte del redondeo descartado.

```python
def suma_compensada(valores):
    total = 0.0
    correccion = 0.0

    for valor in valores:
        ajustado = valor - correccion
        nuevo = total + ajustado
        correccion = (nuevo - total) - ajustado
        total = nuevo

    return total
```

Compare esta función con `sum` y con `math.fsum` en listas que mezclen números muy grandes y muy pequeños. No basta con informar cuál entrega más dígitos: diseñe un caso cuya suma exacta pueda conocerse.

## 7. Condicionamiento y estabilidad

| Idea | Pregunta | Depende principalmente de… |
| --- | --- | --- |
| Condicionamiento | ¿Cuánto cambia la respuesta si cambia un poco la entrada? | El problema matemático |
| Estabilidad | ¿Cuánto error adicional introduce el procedimiento? | El algoritmo y su implementación |
| Convergencia | ¿La aproximación se acerca a la solución al refinar o iterar? | Método, parámetros y supuestos |

Un problema puede estar mal condicionado aunque se use un algoritmo excelente. También puede ocurrir lo contrario: un problema bien condicionado puede resolverse con una formulación inestable.

## 8. Aplicación física: expansión multipolar

El potencial producido por una distribución localizada puede aproximarse mediante una serie de términos multipolares cuando el punto de observación se encuentra suficientemente lejos. Este problema conecta varias ideas de la unidad:

- reemplazar una expresión exacta por una serie truncada;
- estudiar el parámetro que controla la aproximación;
- comparar error de truncamiento y costo;
- evaluar polinomios de Legendre mediante recurrencias;
- reconocer que una reformulación puede evitar una resta delicada en el denominador.

| Pregunta de análisis | Evidencia esperada |
| --- | --- |
| ¿En qué región geométrica converge la expansión? | Relación entre distancia de la fuente y del observador |
| ¿Cuántos términos son necesarios? | Error frente al orden de truncamiento |
| ¿Qué ocurre cerca de la distribución? | Deterioro o pérdida de convergencia |
| ¿Cómo se verifica? | Comparación con el potencial calculado directamente |
| ¿Qué implementación conviene? | Recurrencia estable para los polinomios |

## Tabla de diagnóstico

| Síntoma | Posible causa | Prueba recomendada |
| --- | --- | --- |
| Cambios enormes ante pequeñas perturbaciones | Mal condicionamiento | Perturbar sistemáticamente las entradas |
| El error crece al reducir demasiado el paso | Redondeo y cancelación | Barrido logarítmico del paso |
| Aparecen `inf` o `NaN` | Overflow, dominio inválido o división por cero | Verificar rangos y finitud |
| Dos expresiones equivalentes difieren | Inestabilidad algebraica | Reformular y comparar contra alta precisión |
| La solución parece correcta, pero el residuo es grande | Criterio de parada inadecuado | Calcular la ecuación residual |
| El resultado cambia con el orden de la suma | Pérdida de precisión | Ordenar términos o usar suma compensada |

## Taller propuesto

1. Calcule error absoluto, relativo y porcentual para tres aproximaciones de `π`. Explique por qué el ordenamiento de las aproximaciones no cambia entre error absoluto y relativo en este caso.
2. Estudie la sensibilidad de `T = 2π√(L/g)` frente a perturbaciones en `L` y `g`. Compare propagación lineal y cálculo directo.
3. Determine experimentalmente cuándo `1.0 + h == 1.0` para valores decrecientes de `h`.
4. Construya un ejemplo de absorción al sumar un número pequeño a uno grande.
5. Compare dos expresiones algebraicamente equivalentes para las raíces de una ecuación cuadrática cuando `b²` es mucho mayor que `4ac`.
6. Implemente la serie de `exp(x)` y compare su comportamiento en `x = 20` y `x = -20`. Registre el término de mayor magnitud.
7. Compare `sum`, la suma compensada y `math.fsum` con datos de escala mixta.
8. Perturbe los coeficientes de un polinomio y observe el cambio en sus raíces. Discuta condicionamiento.
9. Diseñe una función `casi_iguales(a, b, atol, rtol)` y pruebe casos cercanos a cero y de gran magnitud.
10. Explique con un contraejemplo por qué “más decimales impresos” no significa “más exactitud”.

## Producto integrador de la unidad

Elabore un informe breve titulado **Anatomía de un error numérico**. Debe incluir:

- una operación o algoritmo que produzca un resultado engañoso;
- una explicación del mecanismo de error;
- una versión reformulada o una estrategia de mitigación;
- una tabla o gráfica de error;
- al menos tres casos de prueba;
- una conclusión que diferencie condicionamiento y estabilidad.

## Lista de comprobación

- [ ] Definí claramente el valor de referencia.
- [ ] Distinguí error absoluto, relativo y residuo.
- [ ] Conservé unidades donde corresponde.
- [ ] Probé diferentes escalas y no solo un caso cómodo.
- [ ] Revisé valores `NaN` e infinitos.
- [ ] Expliqué el mecanismo del error, no solo su tamaño.
- [ ] Justifiqué cualquier tolerancia utilizada.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados sobre error, propagación, punto flotante, compensación y estabilidad.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 2 y apéndice B.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
