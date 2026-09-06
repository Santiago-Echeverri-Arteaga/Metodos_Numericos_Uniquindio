# Unidad 4. Ceros de funciones y minimización

## Sentido de la unidad

Encontrar una raíz significa resolver `f(x)=0`. Muchos problemas físicos adoptan esta forma después de imponer una condición de equilibrio, una ecuación de estado, una restricción geométrica o una relación trascendente. La minimización busca el punto donde una cantidad, como energía o acción discretizada, alcanza un extremo.

Los métodos se diferencian por la información que necesitan, la rapidez de convergencia y sus garantías. La mejor opción no es siempre la que converge en menos iteraciones: también importan el costo de evaluar la función, la disponibilidad de derivadas y la robustez frente a una aproximación inicial imperfecta.

> **Lectura orientadora:** notas de clase, apartados de ceros, convergencia, métodos con y sin intervalo, sistemas no lineales y minimización; Gezerlis, capítulo 5.

## Resultados de aprendizaje

Al terminar la unidad, el estudiante podrá:

- formular problemas físicos como ecuaciones no lineales;
- distinguir métodos con intervalo y métodos abiertos;
- implementar bisección, punto fijo, Newton y secante;
- comparar velocidad, costo y robustez mediante evidencia;
- establecer criterios de parada basados en residuo e intervalo;
- reconocer raíces múltiples y fallos de convergencia;
- extender Newton a sistemas y explicar la idea de métodos cuasi-Newton;
- localizar mínimos unidimensionales mediante sección áurea.

## Secuencia sugerida de clases

| Clase | Pregunta central | Métodos | Evidencia |
| --- | --- | --- | --- |
| 1 | ¿Cómo garantizar que existe una raíz en un intervalo? | Cambio de signo y bisección | Cota de error |
| 2 | ¿Qué significa convergencia de una iteración? | Punto fijo y orden | Cocientes de errores |
| 3 | ¿Cómo acelerar usando información local? | Newton y secante | Comparación costo-convergencia |
| 4 | ¿Qué ocurre con varias incógnitas? | Newton para sistemas y Broyden | Norma del residuo |
| 5 | ¿Cómo buscar un mínimo sin derivadas? | Acotamiento y sección áurea | Reducción del intervalo |
| 6 | ¿Cómo aparece la optimización en física? | Equilibrio, energía y acción | Modelo discretizado |

## 1. Formulación y exploración inicial

Antes de iterar:

1. defina la función y su dominio;
2. identifique discontinuidades y singularidades;
3. estime escalas y unidades;
4. grafique o muestree la función cuando sea posible;
5. determine si se busca una raíz, todas las raíces o una raíz en una región específica.

| Pregunta | Riesgo que evita |
| --- | --- |
| ¿La función está definida en el intervalo? | Confundir una singularidad con una raíz |
| ¿Hay cambio de signo? | Aplicar bisección sin garantía |
| ¿La raíz puede ser tangente? | No detectar raíces de multiplicidad par |
| ¿Cuánto cuesta evaluar `f`? | Elegir un método con demasiadas evaluaciones |
| ¿Se dispone de `f′` confiable? | Usar Newton con una derivada ruidosa o costosa |

## 2. Bisección

Si `f` es continua y `f(a)f(b)<0`, existe al menos una raíz en `[a,b]`. La bisección evalúa el punto medio y conserva la mitad que mantiene el cambio de signo.

c = (a+b)/2

Después de `n` bisecciones, el ancho del intervalo es `(b-a)/2ⁿ`. Esto proporciona una cota explícita sobre la localización de la raíz.

```python
def biseccion(f, a, b, tol=1e-10, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("El intervalo no encierra un cambio de signo")

    historial = []
    for _ in range(max_iter):
        c = 0.5 * (a + b)
        fc = f(c)
        historial.append((a, b, c, fc))

        if abs(fc) <= tol or 0.5 * abs(b - a) <= tol:
            return c, historial

        if fa * fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    raise RuntimeError("No se alcanzó la tolerancia")
```

### Ventajas y limitaciones

| Ventaja | Limitación |
| --- | --- |
| Convergencia garantizada bajo sus hipótesis | Convergencia lineal |
| Cota geométrica del error | Requiere un intervalo con cambio de signo |
| No usa derivadas | Puede omitir raíces sin cambio de signo |

## 3. Iteración de punto fijo

Una ecuación `f(x)=0` puede reescribirse como `x=g(x)`. La iteración es:

xₖ₊₁ = g(xₖ)

La reformulación es decisiva. Expresiones equivalentes pueden generar iteraciones convergentes o divergentes. Cerca de un punto fijo, la condición `|g′(x*)|<1` favorece convergencia local.

### Experimento

Reescriba una misma ecuación de dos maneras y compare las secuencias. Grafique `y=g(x)` junto con `y=x` y relacione la pendiente con el comportamiento observado.

## 4. Método de Newton-Raphson

Newton reemplaza localmente la función por su recta tangente:

xₖ₊₁ = xₖ - f(xₖ)/f′(xₖ)

Cuando la aproximación inicial es adecuada, la raíz es simple y la función es suficientemente suave, la convergencia puede ser cuadrática. Esto significa que el número de cifras correctas puede crecer rápidamente.

| Fortaleza | Riesgo |
| --- | --- |
| Convergencia local muy rápida | Depende de la aproximación inicial |
| Usa geometría local | Falla si la derivada es cero o muy pequeña |
| Puede extenderse a sistemas | Cada paso puede ser costoso |
| Permite analizar multiplicidad | Puede converger a una raíz distinta |

Para raíces múltiples, Newton pierde su convergencia cuadrática usual. Si la multiplicidad `m` es conocida, puede modificarse el paso multiplicando la corrección por `m`.

## 5. Método de la secante

La secante aproxima la derivada con dos valores recientes:

xₖ₊₁ = xₖ - f(xₖ)(xₖ-xₖ₋₁)/[f(xₖ)-f(xₖ₋₁)]

No necesita una derivada explícita y suele converger más rápido que bisección, pero pierde la garantía del intervalo. Debe detectar denominadores pequeños y conservar un máximo de iteraciones.

## 6. Método de Ridder y estrategias híbridas

Los métodos híbridos intentan combinar la seguridad de un intervalo con una actualización más rápida. Ridder construye una transformación que permite una interpolación más efectiva dentro de un intervalo con cambio de signo.

En práctica científica, una estrategia común es:

1. explorar y encerrar la raíz;
2. reducir el intervalo con un método robusto;
3. acelerar con Newton o secante cuando la aproximación sea segura;
4. volver al método de intervalo si el paso sale de la región confiable.

## 7. Criterios de parada

| Criterio | Expresión | Qué controla |
| --- | --- | --- |
| Cambio absoluto | `|xₖ₊₁-xₖ|` | Estabilización en escala absoluta |
| Cambio relativo | `|Δx|/(atol+rtol|x|)` | Estabilización respecto a la escala |
| Residuo | `|f(xₖ)|` | Cumplimiento de la ecuación |
| Intervalo | `|b-a|` | Cota geométrica en métodos con intervalo |
| Límite | `k ≥ max_iter` | Evita iteración indefinida |

Conviene combinar criterios. Un cambio pequeño puede deberse a estancamiento, y un residuo pequeño puede ser engañoso si la función está mal escalada.

## 8. Sistemas no lineales

Para `F(x)=0`, Newton resuelve en cada iteración:

J(xₖ) Δx = -F(xₖ), luego xₖ₊₁ = xₖ + Δx

`J` es la matriz jacobiana. Se resuelve un sistema lineal; no se calcula explícitamente `J⁻¹`. El costo de construir el jacobiano puede ser alto. Métodos como Broyden actualizan una aproximación a la matriz o a su inversa utilizando información de iteraciones previas.

### Diagnósticos mínimos

- norma de `F(xₖ)`;
- norma del paso `Δx`;
- condición aproximada del jacobiano;
- número de evaluaciones de la función;
- sensibilidad a la aproximación inicial.

## 9. Minimización unidimensional

Si solo se puede evaluar una función y se conoce un intervalo donde hay un mínimo unimodal, la búsqueda por sección áurea reduce el intervalo reutilizando una evaluación.

| Método | Requiere derivada | Requiere intervalo | Comentario |
| --- | --- | --- | --- |
| Sección áurea | No | Sí | Robusto para función unimodal |
| Newton para mínimos | Primera y segunda | No necesariamente | Rápido cerca del mínimo, sensible a curvatura |
| Descenso por gradiente | Primera | No | Extensible a varias dimensiones |
| Cuasi-Newton | Gradiente o diferencias | No | Aproxima curvatura |

## 10. Aplicaciones físicas

| Problema | Formulación numérica |
| --- | --- |
| Volumen en una ecuación de estado | Raíz de una ecuación no lineal |
| Punto de equilibrio | Cero de la fuerza o mínimo de energía |
| Ángulo de lanzamiento para alcanzar un blanco | Raíz del error de posición |
| Parámetro de un modelo | Mínimo de una función de costo |
| Trayectoria clásica | Extremo de una acción discretizada |

## Errores frecuentes

| Error | Consecuencia | Prevención |
| --- | --- | --- |
| No revisar continuidad | “Raíz” cerca de una singularidad | Explorar dominio y graficar |
| Usar Newton con derivada pequeña | Paso enorme | Limitar, amortiguar o cambiar de método |
| Detener solo por `Δx` | Falso estancamiento | Revisar también residuo |
| Redondear dentro de la iteración | Pérdida artificial de convergencia | Redondear solo al comunicar |
| Confundir mínimo local con global | Conclusión física incorrecta | Explorar varios intervalos/inicios |
| Contar iteraciones pero no evaluaciones | Comparación de costo incompleta | Registrar llamadas a `f` y `f′` |

## Taller propuesto

1. Calcule cuántas iteraciones de bisección garantizan una tolerancia dada.
2. Implemente bisección con historial y pruebe un caso sin cambio de signo.
3. Construya dos iteraciones de punto fijo para la misma ecuación y compare.
4. Implemente Newton con residuo, tolerancias y máximo de iteraciones.
5. Estudie Newton cerca de una raíz doble.
6. Compare bisección, Newton y secante usando número de evaluaciones.
7. Diseñe un método híbrido que mantenga un intervalo válido.
8. Resuelva un sistema no lineal de dos ecuaciones y grafique sus curvas de nivel.
9. Implemente sección áurea y verifique la reducción del intervalo.
10. Formule una condición física de equilibrio como raíz y como mínimo; compare ambas rutas.

## Producto integrador de la unidad

Seleccione un problema físico no lineal y resuélvalo mediante un método con intervalo y uno abierto. Entregue formulación, dominio, gráfica exploratoria, historial, criterios de parada, costo en evaluaciones, comparación final y discusión de los fallos posibles.

## Lista de comprobación

- [ ] Definí dominio, unidades y región de búsqueda.
- [ ] Verifiqué las hipótesis del método.
- [ ] Registré residuo, cambio e iteraciones.
- [ ] Incluí un máximo de iteraciones.
- [ ] Comparé costo mediante evaluaciones, no solo iteraciones.
- [ ] Probé aproximaciones iniciales alternativas.
- [ ] Interpreté qué representa físicamente la raíz o el mínimo.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados de ceros, convergencia, sistemas no lineales y minimización.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 5.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
