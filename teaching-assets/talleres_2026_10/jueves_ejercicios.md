# Jueves: de las ecuaciones al programa

**8 de octubre de 2026 · Trabajo individual · Dos horas · Hasta 1 punto del segundo parcial**

Resuelve los cinco ejercicios mediante un programa ejecutable. El objetivo es traducir los temas vistos en clase a funciones, ciclos, matrices y controles que permitan obtener e interpretar resultados numéricos. Cada ejercicio pide una construcción propia y una comprobación independiente.

## Material de partida y herramientas

Reutiliza las implementaciones del libro: [Kahan](../../examples/book_original/kahansum.py), [diferencias finitas](../../examples/book_original/finitediff.py), [Richardson](../../examples/book_original/richardsondiff.py), [bisección](../../examples/book_original/bisection.py) y [eliminación gaussiana con pivoteo](../../examples/book_original/gauelim_pivot.py), con su dependencia [sustitución triangular](../../examples/book_original/triang.py).

Puedes importarlas o incorporar las funciones necesarias conservando autor y procedencia. No se exige reescribir esos algoritmos. El desarrollo propio son las funciones que describen los problemas, la construcción de datos y matrices, las adaptaciones, los experimentos y las verificaciones. Trabaja en tu archivo sin modificar los originales del repositorio. Distingue el código reutilizado del código que desarrollaste.

Puedes usar `math`, NumPy y Matplotlib. Los solucionadores de biblioteca pueden servir como contraste; utiliza los algoritmos indicados para producir los resultados solicitados. Organiza el trabajo en funciones reutilizables. Las matrices y los barridos deben generarse mediante código, no introducirse como listas de resultados calculados a mano.

## 1. Acumular datos sin confundir resultado y exactitud

Construye las secuencias A=`[1e16]+[1.0]*1000+[-1e16]` y B=`[1e16,1.0,-1e16]`, cuyas sumas matemáticas son 1000 y 1. Antes de ejecutar, predice si Kahan recuperará ambas sumas.

Escribe una función de comparación que reciba una secuencia y su suma de referencia y devuelva los resultados y errores absolutos de la suma ordinaria y Kahan. Para la ordinaria usa un acumulador y un ciclo; las funciones de biblioteca pueden emplear otras estrategias.

Ejecuta la comparación para A y B, tanto en su orden original como ordenadas por magnitud creciente. Usa una ordenación estable para los empates. Genera una tabla con los ocho resultados. Explica un caso donde la compensación ayuda y otro donde no recupera la suma exacta. Comprueba que ninguna ordenación cambió la cantidad de elementos ni sus valores.

**Desarrollo propio:** función de comparación, generación de casos y tabla automática. **Evidencia:** tabla y conclusión sobre algoritmo, orden y redondeo.

## 2. Convertir el error en una decisión sobre el paso

Elige `a` entre 1, 2 y 3 y programa `f(x)=exp(a*x)` y su derivada de referencia `a*exp(a*x)`. En `x0=0.4`, compara diferencia central y Richardson central para `h=10**(-k)`, con `k=1,...,10`.

Adapta el ejemplo para que una función reciba f, su derivada, el punto y los pasos, y devuelva una tabla de errores y el mejor paso ensayado para cada método. En `calc_cd` del libro, h es la separación total entre los puntos `x±h/2`; conserva esa convención al extrapolar.

Repite el barrido con `f_medida(x)=round(f(x),6)`, manteniendo como referencia la derivada de f. Genera una figura con dos paneles, uno por tipo de evaluación, con error frente a h en escala logarítmica. Identifica los errores nulos sin inventar valores para dibujarlos.

Selecciona método y paso para la lectura redondeada y comprueba esa elección en `x1=0.7`, sin volver a seleccionar h. Compara allí con el mismo método usando h=1e-10. Explica por qué una evaluación con resolución limitada cambia la elección del paso.

**Desarrollo propio:** funciones del problema, barrido reutilizable y selección automática del mejor paso. **Evidencia:** figura, tabla de los cuatro mejores pasos y comprobación en x1.

## 3. Adaptar bisección para entregar una respuesta verificable

Parte de la rutina del libro y adáptala para que valide el intervalo, reconozca raíces exactas en extremos o punto medio, y devuelva raíz, residuo, intervalo final, iteraciones y estado de convergencia. Conserva el algoritmo de bisección. Usa semianchura del intervalo `≤1e-8` como parada, con máximo 100 iteraciones; una raíz exacta permite cerrar el intervalo en ese punto. El residuo se informa como diagnóstico independiente.

Construye una tabla de pruebas y ejecútala mediante un ciclo:

| Función | Intervalo | Resultado esperado |
| --- | --- | --- |
| `x**2-2` | `[1,2]` | Aproximar `sqrt(2)` y encerrar la referencia |
| `x-1` | `[1,2]` | Reconocer la raíz del extremo |
| `x` | `[-1,1]` | Reconocer la raíz del punto medio |
| `x**2+1` | `[-1,1]` | Rechazar el intervalo sin cambio de signo |

Agrega el primer caso con máximo dos iteraciones: debe informar que no alcanzó la tolerancia. Registra los fallos esperados sin detener todo el programa. Comprueba mediante condiciones en el código los resultados esperados, además de imprimirlos. Explica una limitación de la rutina original que tu adaptación resuelve.

**Desarrollo propio:** adaptación de controles y retorno, tabla de casos y verificaciones automáticas. **Evidencia:** resultados de las cinco pruebas y cambios identificados.

## 4. Construir un sistema a partir de sus ecuaciones

Considera n incógnitas que satisfacen

`2*u_i-u_(i-1)-u_(i+1)=b_i`, para `i=1,...,n`, con `u_0=u_(n+1)=0`.

Escribe una función que reciba n y construya la matriz A de este sistema mediante índices y ciclos o diagonales de NumPy. No escribas sus filas manualmente. Para comprobar la construcción, genera `u_ref,i=sin(pi*i/(n+1))` y calcula b **directamente con la fórmula escalar anterior y sus condiciones de frontera**, sin usar `A @ u_ref`. Esta independencia permite detectar errores de índices en A.

Resuelve con la eliminación con pivoteo del libro para n=5 y n=10. Usa arreglos de punto flotante. Reporta `max(abs(A@u-b))` y `max(abs(u-u_ref))`. Comprueba ambos valores frente a 1e-10 e informa si pasan.

Para n=10, aumenta únicamente b_1 en 0.01 y vuelve a resolver. Calcula el cambio máximo en u y el residuo respecto al **nuevo** b. Explica por qué puede cambiar la solución aunque ambos sistemas tengan residuos pequeños.

**Desarrollo propio:** ensamblaje general de A, construcción independiente de b y prueba de perturbación. **Evidencia:** tabla de verificación y cambio observado. El solucionador se reutiliza.

## 5. Traducir un ajuste a ecuaciones normales

Genera nueve abscisas `x_i=-1+i/4`, para `i=0,...,8`, y observaciones

`y_i=1+2*x_i+0.5*x_i**2+0.08*(-1)**i`.

Construye una función que reciba x, y y el grado p, forme la matriz de diseño `V_ij=x_i**j`, para `j=0,...,p`, y obtenga los coeficientes resolviendo `(V.T@V)c=V.T@y` con la eliminación del libro. No uses `polyfit`, `lstsq` ni la inversa para obtener el ajuste solicitado. Reutiliza el solucionador del ejercicio anterior.

Ajusta p=1 y p=2. Programa la evaluación del polinomio a partir del vector de coeficientes. Calcula para cada grado el error cuadrático medio de entrenamiento, `ECM=promedio((P(x_i)-y_i)**2)`.

Comprueba ambos modelos en los ocho puntos intermedios `t_i=-1+(i+0.5)/4`, con `i=0,...,7`, usando como referencia sin perturbación `g(t)=1+2*t+0.5*t**2`. Reporta allí el error absoluto máximo. Elige un grado para representar la tendencia de los datos y sustenta la elección con ambos indicadores. Explica por qué un ajuste no tiene que pasar por todas las observaciones.

**Desarrollo propio:** matriz de diseño, construcción del sistema normal, evaluador polinómico y métricas. **Evidencia:** tabla con coeficientes y errores de los dos modelos, y decisión justificada.

## Entrega y sustentación

Entrega un script o notebook que ejecute los cinco ejercicios, con las tablas y la figura indicadas. Incluye de dos a cuatro frases de interpretación por ejercicio; las explicaciones van junto al código, sin informe separado. Identifica las fuentes y tus adaptaciones.

En la revisión debes explicar cómo una ecuación se convierte en las operaciones de una de tus funciones, justificar una comprobación y anticipar el efecto de cambiar un parámetro. Debes poder ejecutar esa modificación. La sustentación se basa en el mismo trabajo entregado. Ejecutar los ejemplos del libro sin las construcciones y pruebas solicitadas no satisface los ejercicios.

## Rúbrica

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Acumulación · 10 | **10:** comparación automatizada, ocho resultados e interpretación correcta | **7:** comparación válida con una omisión | **3:** resultados aislados | **0:** sin evidencia |
| Derivación · 20 | **20:** cuatro barridos, selección programada, figura y comprobación en x1 | **14:** cálculo correcto con una comprobación pendiente | **6:** derivadas sin estudio del paso | **0:** sin evidencia |
| Bisección · 20 | **20:** adaptación correcta y cinco pruebas con verificaciones automáticas | **14:** raíz válida con un control pendiente | **6:** adaptación sin pruebas suficientes | **0:** sin evidencia |
| Sistema lineal · 20 | **20:** ensamblaje general, referencia independiente, ambos tamaños y perturbación interpretada | **14:** construcción correcta con una comprobación pendiente | **6:** sistema resuelto sin construcción general verificable | **0:** sin evidencia |
| Mínimos cuadrados · 20 | **20:** construcción general del ajuste, evaluación, dos grados y decisión con errores | **14:** ajustes correctos con una comprobación pendiente | **6:** coeficientes sin validación suficiente | **0:** sin evidencia |
| Sustentación y reproducibilidad · 10 | **10:** ejecución completa, atribución y explicación de código, controles y modificación | **7:** explicación coherente con una omisión | **3:** ejecución o explicación incompleta | **0:** no acredita el trabajo |

La valoración `R_j` es sobre 100. El aporte es `J=R_j/100`, hasta **1 punto**. Se aplican las [reglas del segundo parcial](../../assessments/README.md#segundo-parcial-talleres-y-exoneración).
