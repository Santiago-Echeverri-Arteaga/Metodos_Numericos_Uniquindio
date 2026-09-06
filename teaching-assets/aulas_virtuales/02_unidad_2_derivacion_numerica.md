# Unidad 2. Derivación numérica y diferenciación automática

## Sentido de la unidad

En numerosos problemas físicos se conoce una función mediante datos discretos, una simulación costosa o un programa que no ofrece una expresión simbólica sencilla. Aproximar derivadas permite estimar velocidades, aceleraciones, gradientes, sensibilidades y operadores diferenciales, pero exige equilibrar dos errores opuestos: el truncamiento disminuye al reducir el paso y el redondeo puede aumentar.

> **Lectura orientadora:** notas de clase, apartados de derivadas, extrapolación de Richardson y números duales; Gezerlis, capítulo 3.

## Resultados de aprendizaje

Al finalizar la unidad, el estudiante podrá:

- derivar fórmulas de diferencias finitas mediante series de Taylor;
- identificar el orden del error de una aproximación;
- seleccionar un tamaño de paso mediante evidencia;
- construir diferencias de mayor orden;
- aplicar extrapolación de Richardson;
- explicar la idea de diferenciación automática con números duales;
- validar una derivada aproximada contra una referencia conocida;
- aplicar derivación a problemas físicos discretos.

## Secuencia sugerida de clases

| Clase | Pregunta central | Métodos | Producto |
| --- | --- | --- | --- |
| 1 | ¿Cómo aproximar una derivada a partir de valores cercanos? | Adelantada, atrasada y central | Derivación con Taylor |
| 2 | ¿Qué tan pequeño debe ser el paso? | Error de truncamiento y redondeo | Curva de error frente a `h` |
| 3 | ¿Cómo aumentar el orden sin reducir excesivamente el paso? | Plantillas y Richardson | Comparación de órdenes |
| 4 | ¿Se puede derivar un programa sin diferencias? | Números duales y regla de la cadena | Implementación mínima |
| 5 | ¿Cómo se usan derivadas discretas en física? | Datos de movimiento y energía cinética local | Informe de validación |

## 1. Diferencias finitas básicas

Para una función suficientemente suave y un paso `h`, las aproximaciones más comunes son:

Adelantada: f′(x) ≈ [f(x+h) - f(x)] / h

Atrasada: f′(x) ≈ [f(x) - f(x-h)] / h

Central: f′(x) ≈ [f(x+h) - f(x-h)] / (2h)

| Fórmula | Orden de truncamiento | Evaluaciones nuevas | Uso típico |
| --- | --- | --- | --- |
| Adelantada | `O(h)` | 1 o 2 | Extremo izquierdo o datos causales |
| Atrasada | `O(h)` | 1 o 2 | Extremo derecho |
| Central | `O(h²)` | 2 | Puntos interiores y mayor precisión |

El orden indica cómo cambia el error dominante cuando `h` se reduce. Si el método es de orden dos, dividir `h` por dos debería reducir aproximadamente el error de truncamiento por un factor de cuatro, mientras este error sea dominante.

## 2. Derivación mediante Taylor

La serie de Taylor permite expresar `f(x+h)` y `f(x-h)` alrededor de `x`. Al sumar o restar las expansiones se cancelan términos y se obtiene tanto la fórmula como el término dominante del error.

Esta derivación cumple dos propósitos:

1. explica por qué una fórmula aproxima la derivada;
2. permite anticipar la tasa de convergencia antes de programar.

### Actividad guiada

Derive la fórmula central para la primera derivada. Identifique qué términos se cancelan y por qué el error es de orden `h²`. Después derive una aproximación central para la segunda derivada.

f″(x) ≈ [f(x+h) - 2f(x) + f(x-h)] / h²

## 3. El dilema del tamaño de paso

Reducir `h` disminuye el error de truncamiento, pero intensifica la resta entre valores cercanos y la división por un número pequeño. El error total suele presentar una curva en forma de U.

| Región | Comportamiento dominante | Evidencia |
| --- | --- | --- |
| `h` grande | Truncamiento | El error disminuye con la pendiente teórica |
| `h` intermedio | Zona útil | Aparece un mínimo del error |
| `h` extremadamente pequeño | Redondeo y cancelación | El error se estanca o aumenta |

```python
import math

def derivada_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)

x = 1.0
exacta = math.cos(x)

for k in range(1, 17):
    h = 10.0 ** (-k)
    aprox = derivada_central(math.sin, x, h)
    error = abs(aprox - exacta)
    print(k, h, error)
```

El mejor `h` depende de la función, la escala de `x`, la precisión aritmética y la fórmula. Por eso no debe fijarse universalmente como “un número muy pequeño”.

## 4. Plantillas de mayor orden

Usar más puntos permite cancelar más términos de Taylor. Por ejemplo, una plantilla central de cinco puntos puede alcanzar orden cuatro. El beneficio tiene costo: más evaluaciones, mayor sensibilidad a ruido y tratamiento especial en fronteras.

| Decisión | Ventaja | Riesgo |
| --- | --- | --- |
| Más puntos | Mayor orden formal | Más costo y mayor exposición a datos ruidosos |
| Paso menor | Menor truncamiento inicialmente | Más redondeo y cancelación |
| Paso mayor | Menos sensibilidad al ruido | Pérdida de detalle local |
| Ajuste local | Suaviza datos experimentales | Introduce sesgo del modelo elegido |

## 5. Extrapolación de Richardson

Si una aproximación tiene la forma:

D(h) = D + C hᵖ + términos de orden superior

pueden combinarse `D(h)` y `D(h/2)` para cancelar el término principal:

D_R = [2ᵖ D(h/2) - D(h)] / (2ᵖ - 1)

La extrapolación no corrige una fórmula que se encuentre en la zona dominada por redondeo ni garantiza mejora si la expansión asintótica aún no es válida.

### Experimento recomendado

Calcule la derivada de `sin(x)` en `x=1` mediante diferencia adelantada y Richardson. Para una secuencia de pasos, compare el error y estime experimentalmente el orden usando cocientes entre errores consecutivos.

## 6. Diferenciación automática y números duales

La diferenciación automática aplica sistemáticamente la regla de la cadena a las operaciones de un programa. No es diferenciación simbólica ni una diferencia finita.

Un número dual puede representarse como `a + bε`, con `ε² = 0`. Si se evalúa una función suave en `x + ε`, el resultado conserva simultáneamente el valor y la derivada:

f(x + ε) = f(x) + f′(x) ε

### Estructura mínima

```python
class Dual:
    def __init__(self, valor, derivada=0.0):
        self.valor = valor
        self.derivada = derivada

    def __add__(self, otro):
        if not isinstance(otro, Dual):
            otro = Dual(otro)
        return Dual(
            self.valor + otro.valor,
            self.derivada + otro.derivada,
        )

    def __mul__(self, otro):
        if not isinstance(otro, Dual):
            otro = Dual(otro)
        return Dual(
            self.valor * otro.valor,
            self.derivada * otro.valor + self.valor * otro.derivada,
        )
```

Completar la división, potencias y funciones elementales constituye un ejercicio de aplicación de reglas de derivación y diseño de software.

## 7. Datos experimentales

Si se conocen posiciones `x(tᵢ)` en tiempos discretos, la velocidad puede estimarse con diferencias. Sin embargo, derivar amplifica ruido: pequeñas variaciones en posición se dividen por `h`.

| Situación | Estrategia posible | Validación |
| --- | --- | --- |
| Datos uniformes y poco ruidosos | Diferencia central interior | Comparar varios pasos efectivos |
| Extremos del intervalo | Fórmula unilateral | Revisar orden menor |
| Datos no uniformes | Interpolación local o pesos específicos | Caso polinómico conocido |
| Datos ruidosos | Ajuste o suavizado local antes de derivar | Residuos y sensibilidad al ancho de ventana |

## 8. Aplicación física: energía cinética local

En mecánica cuántica, el operador cinético involucra una segunda derivada de la función de onda. Al aproximarla numéricamente se deben tratar con cuidado:

- puntos donde la función de onda es muy pequeña;
- condiciones de frontera;
- normalización;
- error de discretización;
- unidades del operador;
- comparación con una función de onda de solución conocida.

Una implementación físicamente sensata debe estudiar tanto el error de la derivada como el comportamiento de la magnitud derivada.

## Errores frecuentes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Elegir `h` demasiado pequeño sin estudiar el error | Resultado dominado por redondeo | Barrer varios órdenes de magnitud |
| Usar fórmula central en una frontera sin datos externos | Acceso inválido o hipótesis oculta | Emplear fórmula unilateral o condición de frontera |
| Reportar solo un valor de la derivada | No se demuestra confiabilidad | Comparar pasos y calcular error o residuo |
| Ignorar ruido experimental | Derivada altamente oscilante | Ajuste local y análisis de sensibilidad |
| Confundir diferenciación automática con simbólica | Interpretación incorrecta | Seguir el grafo de operaciones y la regla de la cadena |
| Aplicar Richardson sin conocer el orden `p` | Cancelación incorrecta | Derivar o medir el orden primero |

## Taller propuesto

1. Derive las diferencias adelantada, atrasada y central usando Taylor.
2. Para `f(x)=exp(x)`, grafique el error de la diferencia central en `x=1` para `h` entre `10⁻¹` y `10⁻¹⁶`.
3. Estime la pendiente del error en la región de truncamiento.
4. Compare la segunda derivada de `sin(x)` con su valor exacto.
5. Construya una fórmula central de cinco puntos resolviendo las condiciones sobre los coeficientes.
6. Aplique Richardson a una diferencia de orden uno y a una de orden dos.
7. Genere datos sintéticos de posición con ruido y compare velocidades obtenidas con diferentes pasos.
8. Implemente números duales para suma, producto y potencia entera; verifique tres funciones.
9. Compare diferencia finita, paso complejo si está disponible y diferenciación automática para una función sensible.
10. Explique por qué derivar datos suele ser más inestable que integrarlos.

## Producto integrador de la unidad

Construya un **atlas de derivadas numéricas** para una función con derivada conocida. El producto debe contener:

- al menos tres aproximaciones;
- gráfica logarítmica de error contra `h`;
- estimación experimental del orden;
- identificación de las regiones de truncamiento y redondeo;
- costo en evaluaciones de la función;
- recomendación final sustentada.

## Lista de comprobación

- [ ] Derivé o cité el orden de la fórmula utilizada.
- [ ] Estudié más de un tamaño de paso.
- [ ] Separé error de truncamiento y redondeo.
- [ ] Traté explícitamente los extremos del dominio.
- [ ] Validé con una derivada exacta o una referencia independiente.
- [ ] Expliqué el costo en evaluaciones.
- [ ] Interpreté la derivada con sus unidades físicas.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados sobre derivadas, error total, diferencias centrales, Richardson y números duales.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 3.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
