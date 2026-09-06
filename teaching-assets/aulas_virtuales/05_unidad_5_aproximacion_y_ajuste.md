# Unidad 5. Aproximación, interpolación y ajuste

## Sentido de la unidad

En física es frecuente conocer una magnitud solo en puntos discretos. Puede ser necesario estimar valores intermedios, derivar una tabla, integrar datos o construir un modelo que describa una tendencia experimental. La interpolación intenta pasar exactamente por los datos; el ajuste acepta discrepancias y busca representar una relación subyacente.

Confundir ambos objetivos produce modelos engañosos. Esta unidad desarrolla criterios para decidir cuándo interpolar, cuándo ajustar y cómo validar la aproximación.

> **Lectura orientadora:** notas de clase, apartados de aproximación, interpolación polinómica, nodos de Chebyshev y mínimos cuadrados; Gezerlis, capítulo 6.

## Resultados de aprendizaje

Al finalizar la unidad, el estudiante podrá:

- diferenciar interpolación, aproximación y regresión;
- construir interpolantes de Lagrange;
- explicar problemas de la base monomial y de matrices de Vandermonde;
- reconocer el fenómeno de Runge y la utilidad de los nodos de Chebyshev;
- utilizar interpolación por tramos y splines;
- formular mínimos cuadrados lineales y ponderados;
- analizar residuos y evitar extrapolaciones injustificadas;
- seleccionar un modelo según el propósito físico y la calidad de datos.

## Secuencia sugerida de clases

| Clase | Pregunta central | Herramientas | Evidencia |
| --- | --- | --- | --- |
| 1 | ¿Qué significa aproximar datos discretos? | Interpolación frente a ajuste | Tabla de decisión |
| 2 | ¿Cómo construir un polinomio que pase por los datos? | Lagrange y forma baricéntrica | Interpolante validado en nodos |
| 3 | ¿Por qué un polinomio de mayor grado puede ser peor? | Runge, Vandermonde y Chebyshev | Comparación gráfica |
| 4 | ¿Cómo conservar comportamiento local? | Interpolación por tramos y splines | Continuidad y derivadas |
| 5 | ¿Cómo modelar datos con incertidumbre? | Mínimos cuadrados y ponderación | Residuos y parámetros |
| 6 | ¿Cómo validar un modelo? | Separación de datos, residuos y plausibilidad | Informe de decisión |

## 1. Tres objetivos diferentes

| Objetivo | Condición principal | Uso típico |
| --- | --- | --- |
| Interpolación | La curva pasa por cada dato | Tabla considerada exacta o re-muestreo |
| Ajuste | La curva minimiza una discrepancia | Mediciones con ruido |
| Aproximación funcional | Se reemplaza una función compleja por otra manejable | Cálculo, compresión o análisis |

La elección depende de la procedencia de los datos. Si cada punto tiene incertidumbre experimental, obligar a la curva a pasar exactamente por todos puede modelar el ruido en lugar del fenómeno.

## 2. Interpolación polinómica

Dados `n+1` puntos con abscisas distintas, existe un único polinomio de grado a lo sumo `n` que pasa por todos.

La forma de Lagrange es:

P(x) = Σ yᵢ Lᵢ(x), con Lᵢ(xⱼ)=1 si i=j y 0 en otro caso

Cada polinomio cardinal `Lᵢ` selecciona el dato `yᵢ` en su nodo y se anula en los demás.

### Comprobaciones esenciales

- `P(xᵢ)` debe coincidir con `yᵢ` dentro de la tolerancia;
- no debe haber abscisas repetidas;
- las unidades de `P` deben ser las de `y`;
- la evaluación debe estudiarse dentro y fuera del intervalo de datos;
- la precisión no se demuestra solo verificando los nodos.

## 3. Base monomial y matriz de Vandermonde

También puede escribirse:

P(x) = c₀ + c₁x + c₂x² + … + cₙxⁿ

Determinar los coeficientes produce un sistema con matriz de Vandermonde. Aunque la representación es válida, puede estar mal condicionada para grados altos o nodos desfavorables.

| Representación | Ventaja | Riesgo |
| --- | --- | --- |
| Monomios | Familiar y directa | Condicionamiento pobre |
| Lagrange | Construcción conceptual clara | Evaluación ingenua costosa |
| Baricéntrica | Evaluación estable y eficiente | Requiere pesos bien construidos |
| Newton dividido | Permite añadir nodos progresivamente | Depende del orden y escalamiento |

## 4. Error de interpolación

Para una función suficientemente suave, el error incluye el producto de las distancias a los nodos:

f(x)-P(x) = f⁽ⁿ⁺¹⁾(ξ)/(n+1)! · Π(x-xᵢ)

Esta expresión muestra que el error depende de la función, del número de nodos y de su ubicación. Aumentar el grado no garantiza una mejora uniforme.

## 5. Fenómeno de Runge y nodos de Chebyshev

Con nodos equiespaciados, ciertos interpolantes de alto grado oscilan fuertemente cerca de los extremos. Los nodos de Chebyshev concentran más puntos en esas regiones y reducen el máximo del producto nodal.

### Experimento recomendado

Interpole una función suave con curvatura intensa usando:

1. nodos equiespaciados;
2. nodos de Chebyshev;
3. spline cúbico.

Compare error máximo, comportamiento en extremos y costo. No use únicamente la figura: incluya una métrica cuantitativa sobre una malla densa.

## 6. Interpolación por tramos y splines

Un spline cúbico utiliza polinomios de bajo grado en subintervalos y exige continuidad de la función y de ciertas derivadas.

| Método | Continuidad | Ventaja | Limitación |
| --- | --- | --- | --- |
| Lineal por tramos | Función continua | Simple y no oscila demasiado | Derivada discontinua en nodos |
| Cúbico por tramos | Depende de construcción | Mayor suavidad | Requiere condiciones de frontera |
| Spline cúbico | Usualmente hasta segunda derivada | Buen equilibrio local-global | Extrapolación sigue siendo riesgosa |

Las condiciones “natural”, “sujeta” u otras cambian el comportamiento en los extremos. Deben elegirse de acuerdo con la información física disponible.

## 7. Mínimos cuadrados lineales

Para un modelo lineal en los parámetros, se busca minimizar:

S(c) = Σ [yᵢ - modelo(xᵢ;c)]²

Un modelo puede ser lineal en parámetros aunque no sea lineal en `x`. Por ejemplo, `c₀ + c₁x + c₂x²` es lineal respecto a `c₀`, `c₁` y `c₂`.

Las ecuaciones normales tienen la forma:

Aᵀ A c = Aᵀ y

Formar `AᵀA` puede empeorar el condicionamiento. En cálculos serios suelen preferirse QR o SVD, especialmente cuando las columnas de `A` son casi dependientes.

## 8. Ajuste ponderado

Si cada medición tiene una incertidumbre estándar `σᵢ`, una discrepancia habitual es:

χ² = Σ [(yᵢ-modelo(xᵢ))/σᵢ]²

Los pesos solo son justificables si representan la calidad de los datos. Usar pesos arbitrarios para “mejorar” la gráfica cambia el problema sin una base experimental.

## 9. Análisis de residuos

rᵢ = yᵢ - modelo(xᵢ)

| Patrón del residuo | Posible interpretación |
| --- | --- |
| Dispersión aleatoria alrededor de cero | Modelo compatible con la tendencia |
| Curvatura sistemática | Falta estructura en el modelo |
| Amplitud creciente | Varianza no constante |
| Puntos aislados extremos | Datos atípicos o error de registro |
| Bloques correlacionados | Dependencia temporal o espacial ignorada |

Una buena métrica global puede ocultar un patrón. Por eso debe acompañarse de una gráfica de residuos y una discusión física.

## 10. Extrapolación

Interpolar entre datos y extrapolar fuera del intervalo no son operaciones equivalentes. Un modelo puede describir muy bien la región observada y fallar rápidamente fuera de ella.

Antes de extrapolar, pregunte:

- ¿el modelo expresa una ley física o solo una tendencia empírica?;
- ¿cambia el régimen físico fuera del intervalo?;
- ¿cuánto crece la incertidumbre?;
- ¿existen límites o comportamientos asintóticos conocidos?;
- ¿la predicción puede validarse con datos adicionales?

## 11. Aplicación física: contraste de la ley de Stefan–Boltzmann

Una aplicación integradora consiste en analizar mediciones de potencia radiada y temperatura para contrastar una dependencia proporcional a la cuarta potencia de la temperatura. El interés no es obtener una recta bonita, sino decidir qué transformación y qué modelo respetan la física.

| Decisión | Pregunta |
| --- | --- |
| Variables | ¿Se ajusta `P` contra `T⁴`, o se linealizan logaritmos? |
| Incertidumbre | ¿Cómo cambia al transformar los datos? |
| Parámetros | ¿Qué significado físico tienen pendiente e intercepto? |
| Residuos | ¿Aparece curvatura o un sesgo sistemático? |
| Validación | ¿El exponente estimado es compatible con cuatro? |
| Limitaciones | ¿Se han ignorado pérdidas, emisividad o fondo térmico? |

Este caso permite comparar un ajuste basado en la ley física con un polinomio puramente descriptivo y discutir por qué menor residuo no siempre implica mejor modelo científico.

## Errores frecuentes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Interpolar mediciones ruidosas con grado alto | Sobreajuste y oscilaciones | Ajuste o spline con criterio |
| Formar Vandermonde sin escalar | Condicionamiento pobre | Centrar/escalar o usar otra base |
| Validar solo en nodos | Error cero por construcción | Evaluar entre nodos |
| Elegir grado por apariencia | Decisión subjetiva | Residuos y validación |
| Formar ecuaciones normales sin revisar condición | Pérdida de cifras | QR o SVD |
| Extrapolar sin advertencia | Predicción no sustentada | Limitar dominio y reportar incertidumbre |

## Taller propuesto

1. Construya a mano un interpolante de Lagrange para tres puntos.
2. Verifique computacionalmente la propiedad cardinal.
3. Compare base monomial y forma baricéntrica en nodos crecientes.
4. Reproduzca el fenómeno de Runge con nodos equiespaciados.
5. Sustituya los nodos por Chebyshev y cuantifique la mejora.
6. Compare interpolación lineal, polinómica global y spline cúbico.
7. Ajuste una recta a datos con incertidumbre igual y desigual.
8. Resuelva un ajuste polinómico con ecuaciones normales, QR y SVD; compare residuos y sensibilidad.
9. Genere una gráfica de residuos y diagnostique su patrón.
10. Diseñe un ejemplo donde interpolación y ajuste respondan preguntas diferentes.

## Producto integrador de la unidad

Analice un conjunto pequeño de datos físicos mediante un interpolante y un ajuste. Compare propósito, error dentro del intervalo, residuos, sensibilidad al número de puntos y extrapolación. Finalice con una recomendación argumentada sobre cuál representación debe usarse y para qué.

## Lista de comprobación

- [ ] Expliqué si los datos se consideran exactos o inciertos.
- [ ] Justifiqué interpolación o ajuste.
- [ ] Revisé condicionamiento y escalamiento.
- [ ] Validé entre nodos o con datos separados.
- [ ] Analicé residuos, no solo una métrica global.
- [ ] Delimité cualquier extrapolación.
- [ ] Conservé unidades y significado de parámetros.

## Fuentes para esta unidad

- Santiago Echeverri Arteaga, *Notas de clase: Métodos Numéricos*, apartados de aproximación, interpolación y mínimos cuadrados.
- Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición, capítulo 6.

---

**Material de referencia:** notas de clase de Métodos Numéricos, acta de concertación 2026-2 y Alex Gezerlis, *Numerical Methods in Physics with Python*, 2.ª edición (Cambridge University Press, 2023). Consulte los PDF adjuntos en Moodle.
