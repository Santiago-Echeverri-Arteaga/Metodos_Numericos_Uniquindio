# Unidad 6. Integración numérica y Monte Carlo

## Sentido de la unidad

La integración numérica aparece cuando una antiderivada no puede expresarse de manera útil, cuando la función es costosa o cuando solo se conocen datos discretos. Las reglas de cuadratura sustituyen el área por una combinación ponderada de evaluaciones. La calidad depende de la suavidad, el tamaño de paso, los nodos y la estructura del integrando.

Esta unidad compara métodos de Newton-Cotes, integración adaptativa, extrapolación, cuadratura de Gauss y Monte Carlo.

> **Lectura orientadora:** notas de clase, apartados de integrales, trapecio, Simpson, adaptación, Gauss-Legendre y números aleatorios; Gezerlis, capítulo 7.

## Resultados de aprendizaje

Al finalizar la unidad, el estudiante podrá:

- derivar reglas de integración a partir de interpolación;
- implementar trapecio y Simpson compuestos;
- relacionar el orden teórico con convergencia observada;
- construir un criterio de refinamiento y adaptación;
- explicar la idea de extrapolación de Romberg;
- usar cuadratura de Gauss-Legendre;
- estimar integrales mediante Monte Carlo y reportar incertidumbre;
- elegir un método según dimensión, suavidad y costo de la función.

## Secuencia sugerida de clases

| Clase | Pregunta central | Métodos | Evidencia |
| --- | --- | --- | --- |
| 1 | ¿Cómo convertir el área en una suma? | Rectángulos y trapecio | Derivación geométrica |
| 2 | ¿Cómo aumentar el orden? | Simpson y Newton-Cotes | Estudio de convergencia |
| 3 | ¿Cómo concentrar esfuerzo donde se necesita? | Cuadratura adaptativa | Partición resultante |
| 4 | ¿Cómo eliminar el término principal del error? | Richardson y Romberg | Tabla triangular |
| 5 | ¿Cómo elegir nodos más eficientes? | Gauss-Legendre | Comparación por evaluaciones |
| 6 | ¿Qué hacer en alta dimensión? | Monte Carlo | Estimación e incertidumbre |

## 1. Integración por interpolación

Muchas reglas se obtienen aproximando `f(x)` por un polinomio local e integrando ese polinomio exactamente.

| Aproximación local | Regla resultante | Orden global típico |
| --- | --- | --- |
| Constante | Rectángulo | Depende del punto escogido |
| Lineal | Trapecio | `O(h²)` |
| Cuadrática | Simpson | `O(h⁴)` |

El orden global supone una función suficientemente suave y una malla regular. Discontinuidades, singularidades o cambios rápidos alteran el comportamiento.

## 2. Regla compuesta del trapecio

Para una partición uniforme con `n` subintervalos y `h=(b-a)/n`:

I_T = h [f(a)/2 + Σ f(a+ih) + f(b)/2]

```python
def trapecio_compuesto(f, a, b, n):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return h * total
```

Una prueba básica debe incluir funciones constantes y lineales, que la regla integra exactamente salvo redondeo.

## 3. Regla compuesta de Simpson

Simpson combina tres puntos y requiere un número par de subintervalos:

I_S = h/3 [f(x₀)+4Σf(x_impar)+2Σf(x_par)+f(xₙ)]

| Método | Exacto para polinomios hasta grado | Requisito |
| --- | --- | --- |
| Trapecio | 1 | `n ≥ 1` |
| Simpson | 3 | `n` par |

La exactitud polinómica no significa que cualquier función sea integrada exactamente. Sirve como prueba y como indicador del orden.

## 4. Estudio de convergencia

Con una solución de referencia `I`, calcule `E(h)=|I_h-I|`. Si `E(h)≈C hᵖ`, entonces:

p ≈ log(E(h)/E(h/2)) / log(2)

| Cantidad a registrar | Razón |
| --- | --- |
| Número de subintervalos | Mide refinamiento |
| Número de evaluaciones | Mide costo real |
| Aproximación | Permite observar estabilización |
| Error o estimador | Mide calidad |
| Orden observado | Contrasta teoría e implementación |

## 5. Integración adaptativa

Una malla uniforme desperdicia evaluaciones en regiones suaves y puede resultar insuficiente donde la función cambia rápidamente. Un método adaptativo:

1. calcula una aproximación en un intervalo;
2. divide el intervalo;
3. compara la aproximación gruesa y la refinada;
4. acepta o subdivide según una tolerancia local;
5. combina las contribuciones aceptadas.

La tolerancia global debe distribuirse de forma coherente. También debe existir una profundidad máxima para evitar recursión indefinida cerca de singularidades.

## 6. Romberg

La integración de Romberg aplica extrapolación de Richardson a aproximaciones del trapecio con pasos sucesivamente menores. Construye una tabla donde cada columna cancela un término adicional del error.

| Ventaja | Limitación |
| --- | --- |
| Reutiliza evaluaciones | Requiere integrando suave |
| Aumenta el orden sistemáticamente | Puede engañar cerca de singularidades |
| Produce estimadores internos | La tabla puede estancarse por redondeo |

## 7. Cuadratura de Gauss-Legendre

En lugar de usar nodos equiespaciados, la cuadratura gaussiana elige nodos y pesos para integrar exactamente polinomios del mayor grado posible con un número dado de evaluaciones.

∫₋₁¹ f(x) dx ≈ Σ wᵢ f(xᵢ)

Para un intervalo `[a,b]` se realiza un cambio lineal de variable. Los nodos son ceros de polinomios ortogonales de Legendre.

| Aspecto | Newton-Cotes | Gauss-Legendre |
| --- | --- | --- |
| Nodos | Generalmente equiespaciados | Elegidos óptimamente |
| Reutilización con datos tabulados | Natural | Puede requerir interpolación |
| Exactitud por evaluación | Menor | Alta para funciones suaves |
| Interpretación | Geométrica y directa | Basada en ortogonalidad |

## 8. Monte Carlo

Si `X` es uniforme en `[a,b]`, entonces:

∫ₐᵇ f(x) dx = (b-a) E[f(X)]

Con `N` muestras, la integral se estima mediante el promedio. El error estadístico típico disminuye como `1/√N`, mucho más lentamente que los métodos deterministas en una dimensión, pero la tasa es menos sensible a la dimensión.

```python
import numpy as np

def integral_monte_carlo(f, a, b, n, semilla=1234):
    rng = np.random.default_rng(semilla)
    x = rng.uniform(a, b, size=n)
    valores = f(x)
    estimacion = (b - a) * valores.mean()
    error_est = (b - a) * valores.std(ddof=1) / np.sqrt(n)
    return estimacion, error_est
```

### Reproducibilidad y aleatoriedad

- use un generador moderno;
- registre la semilla;
- no reinicie la semilla dentro de un ciclo de réplicas;
- estudie correlaciones cuando construya su propio generador;
- no confunda incertidumbre estadística con error sistemático del integrando o modelo.

## 9. Selección del método

| Situación | Método inicial razonable |
| --- | --- |
| Datos tabulados uniformes | Trapecio compuesto |
| Función suave y barata en 1D | Simpson o Gauss-Legendre |
| Función con regiones localizadas difíciles | Adaptativo |
| Se requiere alta precisión en función suave | Gauss o Romberg |
| Dominio de alta dimensión | Monte Carlo o variantes |
| Singularidad conocida | Cambio de variable o partición especializada |
| Oscilación rápida | Método especializado o análisis de fase |

## 10. Aplicación física: Monte Carlo variacional

En mecánica cuántica variacional se propone una función de prueba dependiente de parámetros y se estima el valor esperado de la energía. Monte Carlo permite muestrear configuraciones relevantes cuando la integral tiene dimensión alta.

| Componente | Función dentro del cálculo |
| --- | --- |
| Función de prueba | Define la distribución y los parámetros a optimizar |
| Muestreador | Genera configuraciones representativas |
| Energía local | Construye el estimador de energía |
| Promedio y varianza | Entregan estimación e incertidumbre |
| Tiempo de autocorrelación | Indica cuántas muestras son realmente independientes |
| Optimización | Busca parámetros con menor energía estimada |

Una semilla reproducible no elimina la correlación ni el sesgo de una cadena mal equilibrada. Deben examinarse calentamiento, independencia efectiva, varianza y estabilidad del estimador.

## Errores frecuentes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Usar Simpson con `n` impar | Pesos incorrectos | Validar el parámetro |
| Refinar sin contar evaluaciones | Comparación injusta | Medir costo real |
| Aplicar método estándar sobre singularidad | Convergencia lenta o fallo | Dividir o transformar |
| Aceptar coincidencia entre dos mallas | Posible falsa convergencia | Añadir referencia independiente |
| Reportar Monte Carlo sin incertidumbre | Resultado incompleto | Estimar error estándar |
| Cambiar semilla sin registrarla | Resultado no reproducible | Fijar y documentar |

## Taller propuesto

1. Derive la regla del trapecio integrando el interpolante lineal.
2. Implemente trapecio y verifique funciones constantes y lineales.
3. Implemente Simpson y verifique polinomios hasta grado tres.
4. Estime el orden observado para una función suave.
5. Compare métodos por error frente a número de evaluaciones.
6. Implemente una versión adaptativa y visualice los subintervalos.
7. Construya una tabla de Romberg y detecte estancamiento.
8. Use Gauss-Legendre con diferentes números de nodos.
9. Estime `π` mediante Monte Carlo y compruebe la tasa `1/√N`.
10. Compare cuadratura determinista y Monte Carlo en una y varias dimensiones.

## Producto integrador de la unidad

Resuelva una integral física mediante tres métodos de familias diferentes. Incluya cambio de unidades si se requiere, solución o referencia confiable, error frente a costo, orden observado, tratamiento de singularidades y recomendación del método más apropiado.

## Lista de comprobación

- [ ] Revisé dominio, suavidad y singularidades.
- [ ] Verifiqué requisitos como paridad de `n`.
- [ ] Conté evaluaciones de la función.
- [ ] Estudié convergencia o incertidumbre.
- [ ] No confundí estimador interno con error exacto.
- [ ] Registré semilla en Monte Carlo.
- [ ] Interpreté el resultado con unidades físicas.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados de Newton-Cotes, integración adaptativa, Gauss-Legendre y aleatoriedad.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 7.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
