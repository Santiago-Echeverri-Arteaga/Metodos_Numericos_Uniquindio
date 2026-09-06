# Unidad 7. Ecuaciones diferenciales numéricas

## Sentido de la unidad

Las ecuaciones diferenciales describen evolución, equilibrio, transporte y oscilación. Cuando no existe solución analítica o el modelo incluye condiciones complejas, la solución se aproxima sobre una malla. El resultado depende del paso, del método, de la estabilidad y de la forma de imponer condiciones iniciales o de frontera.

Esta unidad introduce problemas de valores iniciales, sistemas de ecuaciones, estabilidad, métodos de Runge-Kutta y una visión general de problemas de frontera, valores propios y ecuaciones diferenciales parciales.

> **Lectura orientadora:** notas de clase, apartados finales de ecuaciones diferenciales, Euler, error y Runge-Kutta; Gezerlis, capítulo 8.

## Resultados de aprendizaje

Al finalizar la unidad, el estudiante podrá:

- clasificar problemas de valores iniciales, frontera y valores propios;
- transformar ecuaciones de orden superior en sistemas de primer orden;
- implementar Euler hacia adelante y métodos Runge-Kutta;
- distinguir error local y global;
- estudiar convergencia mediante refinamiento temporal;
- reconocer restricciones de estabilidad;
- validar soluciones mediante exactitud, residuos e invariantes;
- describir estrategias básicas para problemas de frontera y ecuaciones parciales.

## Secuencia sugerida de clases

| Clase | Pregunta central | Métodos | Evidencia |
| --- | --- | --- | --- |
| 1 | ¿Qué información define una solución? | IVP, BVP y EVP | Clasificación de problemas |
| 2 | ¿Cómo avanzar desde un estado conocido? | Euler hacia adelante | Derivación y tabla de pasos |
| 3 | ¿Cómo mejorar precisión y estabilidad? | Heun, punto medio y RK4 | Comparación de órdenes |
| 4 | ¿Cómo resolver ecuaciones de orden superior? | Sistemas simultáneos | Oscilador armónico |
| 5 | ¿Qué significa estabilidad? | Ecuación de prueba y paso crítico | Mapa de comportamiento |
| 6 | ¿Cómo tratar condiciones en dos extremos? | Disparo y diferencias finitas | Residuo de frontera |
| 7 | ¿Cómo extenderse al espacio? | Mallas y PDE | Esquema conceptual |

## 1. Clasificación de problemas

| Tipo | Información dada | Ejemplo |
| --- | --- | --- |
| Valor inicial (IVP) | Estado completo en un punto inicial | Posición y velocidad inicial de una partícula |
| Frontera (BVP) | Condiciones en puntos distintos | Temperatura fijada en dos extremos |
| Valor propio (EVP) | Condiciones admitidas solo para ciertos parámetros | Estados estacionarios de Schrödinger |
| Ecuación parcial (PDE) | Dependencia de varias variables independientes | Difusión, ondas o Poisson |

No todos los métodos sirven para todos los tipos. Euler y Runge-Kutta son naturalmente métodos de avance para valores iniciales.

## 2. Problema de valores iniciales

Considere:

y′(t) = f(t,y), con y(t₀)=y₀

Un método produce aproximaciones `yₙ≈y(tₙ)` en una malla `tₙ=t₀+nh`.

Antes de programar deben definirse:

- intervalo de integración;
- estado inicial;
- paso o tolerancia;
- método;
- cantidades diagnósticas;
- criterio de fallo.

## 3. Euler hacia adelante

Euler reemplaza la solución local por su tangente:

yₙ₊₁ = yₙ + h f(tₙ,yₙ)

```python
import numpy as np

def euler(f, t0, y0, h, n):
    t = np.empty(n + 1)
    y = np.empty(n + 1, dtype=float)
    t[0], y[0] = t0, y0

    for k in range(n):
        t[k + 1] = t[k] + h
        y[k + 1] = y[k] + h * f(t[k], y[k])

    return t, y
```

Euler tiene error local de orden `h²` y error global de orden `h`. La diferencia importa: se realizan aproximadamente `1/h` pasos y los errores locales se acumulan.

## 4. Métodos Runge-Kutta

Los métodos Runge-Kutta combinan varias pendientes dentro de un paso para alcanzar mayor orden sin calcular derivadas analíticas de `f`.

| Método | Evaluaciones por paso | Orden global típico |
| --- | --- | --- |
| Euler | 1 | 1 |
| Punto medio / RK2 | 2 | 2 |
| Heun | 2 | 2 |
| RK4 clásico | 4 | 4 |

Para RK4:

k₁=f(tₙ,yₙ), k₂=f(tₙ+h/2,yₙ+hk₁/2), k₃=f(tₙ+h/2,yₙ+hk₂/2), k₄=f(tₙ+h,yₙ+hk₃)

yₙ₊₁ = yₙ + h(k₁+2k₂+2k₃+k₄)/6

Un orden mayor no elimina restricciones de estabilidad ni garantiza mejor resultado si el modelo es rígido.

## 5. Ecuaciones de orden superior como sistemas

Para `x″=g(t,x,x′)`, defina `v=x′`:

x′=v, v′=g(t,x,v)

El estado es el vector `[x,v]`. Esta forma permite aplicar el mismo integrador a múltiples ecuaciones simultáneas.

### Ejemplo: oscilador armónico

x′=v, v′=-ω²x

La energía `E=(v²+ω²x²)/2` es constante en la solución exacta. Su deriva numérica constituye un diagnóstico más informativo que una gráfica visualmente sinusoidal.

## 6. Convergencia temporal

Si no se conoce la solución exacta, compare soluciones con `h`, `h/2` y `h/4` en tiempos comunes. Para un método de orden `p`, la diferencia debería disminuir aproximadamente por `2ᵖ` en el régimen asintótico.

| Evidencia | Qué permite concluir |
| --- | --- |
| Error frente a solución exacta | Convergencia directa |
| Diferencia entre refinamientos | Estimación sin exacta |
| Invariante físico | Calidad cualitativa a largo plazo |
| Residuo discreto | Cumplimiento del esquema |
| Comparación entre métodos | Detección de errores de implementación |

## 7. Estabilidad

Para la ecuación de prueba `y′=λy`, Euler produce:

yₙ₊₁ = (1+hλ)yₙ

Si la solución física decae, el factor numérico también debe permanecer dentro de una región estable. Un paso demasiado grande puede generar oscilaciones o crecimiento artificial.

| Síntoma | Posible causa |
| --- | --- |
| La solución crece cuando debería decaer | Inestabilidad del método o paso excesivo |
| Oscilaciones no físicas | Región de estabilidad inadecuada |
| Se requiere un paso diminuto por una escala rápida | Rigidez |
| RK4 falla aunque su orden es alto | El paso está fuera de su región de estabilidad |

Para problemas rígidos pueden ser necesarios métodos implícitos o integradores especializados.

## 8. Paso adaptativo

Un integrador adaptativo compara dos aproximaciones de diferente orden o dos resoluciones del mismo paso para estimar el error local. Luego acepta, rechaza y ajusta `h`.

Un controlador debe considerar:

- tolerancias absoluta y relativa;
- escalas diferentes entre componentes;
- límites mínimo y máximo de paso;
- número de pasos rechazados;
- eventos o discontinuidades;
- prevención de ciclos infinitos.

## 9. Problemas de frontera

En un BVP las condiciones se especifican en puntos distintos. Dos estrategias introductorias son:

| Estrategia | Idea | Diagnóstico |
| --- | --- | --- |
| Disparo | Convertir una condición desconocida inicial en un parámetro y ajustar la condición final | Residuo en la frontera |
| Diferencias finitas | Discretizar la ecuación en toda la malla y resolver un sistema | Residuo interior y condiciones |

El disparo puede ser sensible cuando pequeñas variaciones iniciales crecen mucho. La formulación matricial puede ser más robusta, pero produce sistemas grandes.

## 10. Valores propios y ecuaciones parciales

Algunas condiciones de frontera solo admiten soluciones no triviales para ciertos valores de un parámetro. Tras discretizar, el problema suele convertirse en uno matricial:

A u = λ u

En ecuaciones parciales se discretizan espacio, tiempo o ambos. Deben revisarse consistencia, estabilidad y convergencia, además de condiciones iniciales y de frontera.

| PDE | Estructura típica | Riesgo numérico |
| --- | --- | --- |
| Difusión | Evolución disipativa | Restricción de paso en esquema explícito |
| Ondas | Propagación | Relación entre paso temporal y espacial |
| Poisson | Problema elíptico | Sistema lineal grande |
| Schrödinger | Evolución compleja o EVP | Conservación de norma y fase |

## 11. Aplicación física: ecuación de Poisson en dos dimensiones

La ecuación de Poisson relaciona una fuente con un campo potencial. En una malla rectangular, el laplaciano se aproxima mediante diferencias finitas y el problema interior se transforma en un sistema lineal grande.

| Etapa | Pregunta de control |
| --- | --- |
| Dominio | ¿Cuál es la geometría y dónde se ubican las fuentes? |
| Frontera | ¿Se prescribe el potencial, su derivada o una combinación? |
| Malla | ¿Cómo se relacionan `Δx` y `Δy` con las escalas físicas? |
| Operador | ¿La plantilla discreta reproduce funciones de prueba? |
| Solución | ¿Conviene método directo, iterativo o disperso? |
| Verificación | ¿Disminuye el residuo y converge al refinar la malla? |

Una visualización del potencial debe acompañarse de cortes, unidades, escala de color y alguna comprobación cuantitativa. Una superficie suave no demuestra que se hayan impuesto correctamente las condiciones de frontera.

## Errores frecuentes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Confundir error local y global | Orden informado incorrectamente | Analizar acumulación de pasos |
| Comparar soluciones en tiempos distintos | Diferencia sin sentido | Interpolar o usar mallas anidadas |
| Elegir paso solo por apariencia | Falsa confianza | Estudio de convergencia |
| Ignorar estabilidad | Crecimiento numérico | Analizar región y escalas |
| Resolver una ecuación de segundo orden como escalar | Estado incompleto | Convertir a sistema de primer orden |
| No comprobar invariantes | Error físico oculto | Registrar energía, norma u otra cantidad |

## Taller propuesto

1. Derive Euler desde Taylor y distinga error local y global.
2. Implemente Euler para decaimiento exponencial y mida el orden.
3. Compare Euler, punto medio y RK4 por error frente a evaluaciones.
4. Explore estabilidad de Euler para varios valores de `hλ`.
5. Resuelva el oscilador armónico y grafique la deriva de energía.
6. Convierta un péndulo no lineal en sistema de primer orden.
7. Compare pasos fijos y adaptativos en una solución con escalas variables.
8. Resuelva un BVP sencillo por disparo y mida el residuo final.
9. Discretice una segunda derivada y formule un problema de valores propios.
10. Explique qué evidencia necesitaría para confiar en una simulación sin solución exacta.

## Producto integrador de la unidad

Construya una simulación de un sistema físico descrito por una EDO. Compare al menos dos métodos y tres pasos, mida convergencia, registre una cantidad física diagnóstica y discuta precisión, estabilidad y costo.

## Lista de comprobación

- [ ] Clasifiqué correctamente el tipo de problema.
- [ ] Definí estado, intervalo y condiciones.
- [ ] Convertí órdenes superiores a un sistema coherente.
- [ ] Estudié más de un paso.
- [ ] Diferencié error local y global.
- [ ] Revisé estabilidad y posibles escalas rápidas.
- [ ] Usé una solución exacta, refinamiento o invariante para validar.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados finales sobre ecuaciones diferenciales, Euler, error y Runge-Kutta.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 8.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
