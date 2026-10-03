# Miércoles: laboratorio computacional de métodos numéricos

**7 de octubre de 2026 · Sesión de dos horas · Trabajo individual · Hasta 1 punto del segundo parcial**

En este taller llevaremos los temas vistos en clase a experimentos computacionales: programar, cambiar una condición, medir qué ocurre y explicar el resultado.

**Entrega exactamente tres experimentos: el 1 y dos a elección entre 2, 3, 4 y 5.** Todos tienen el mismo valor. No es necesario completar los cinco. Las ampliaciones son de consulta, no dan puntos adicionales y no se requieren para obtener la máxima nota ni la exoneración.

Usa un notebook o script con NumPy, SciPy y Matplotlib. Puedes reutilizar tus rutinas de clase y las del [módulo de apoyo](miercoles_apoyo.py), indicando su procedencia. Completa únicamente las funciones de la [plantilla](miercoles_base.py) correspondientes a tus elecciones. No se requiere implementar todos los métodos desde cero.

## 1. Aritmética confiable · Obligatorio

Compara `sqrt(1+x)-1` con `x/(sqrt(1+x)+1)` para `x=10**(-k)`, `k=1,...,16`. Calcula el error relativo de la primera usando la forma racionalizada como referencia numérica estable. Reporta el primer valor ensayado para el que la resta devuelve cero y explica la pérdida de información.

Implementa o adapta tu suma de Kahan y compárala con un ciclo ordinario sobre `[1e16]+[1.0]*n+[-1e16]`, con `n=10,100,1000`. Guarda resultado y error absoluto respecto a n. No uses `sum` para representar la suma ingenua, porque su implementación puede variar entre versiones.

**Entrega:** una gráfica o tabla del barrido, una tabla de las sumas y una conclusión de tres a cinco frases. Explica qué corrige Kahan y qué no corrige.

**Ampliación no evaluada:** clasificar overflow y underflow con `1e308*1e308` y `1e-200*1e-200`; experimentar con propagación de error en `v=d/t` para `d=10±0.1` y `t=2±0.02`.

## 2. Elegir el paso de una derivada · Electivo

Completa diferencia central y Richardson en la plantilla. Para `f(x)=exp(x)` en `x=0`, compara **derecha de dos puntos, central y Richardson**, usando `h=10**(-k)`, `k=1,...,12`. La referencia es `f'(0)=1`; la fórmula lateral está disponible en el módulo de apoyo.

Grafica error absoluto contra h en escala logarítmica, identifica el mejor h ensayado de cada fórmula y estima el orden con los dos primeros errores no nulos. Si un error vale cero, señálalo sin inventar un valor para la gráfica. Explica el comportamiento al reducir demasiado h y distingue orden de precisión de orden de derivación.

**Entrega:** funciones, una figura, tabla de mejor paso y conclusión de tres a cinco frases.

**Ampliación no evaluada:** incluir las otras fórmulas laterales, segunda derivada o una evaluación con números duales de `p(x)=x³+2x`.

## 3. Una solución y su convergencia · Electivo

Usa `A=[[0,2,1],[2,1,0],[1,0,2]]` y `b=[7,4,7]`. El módulo suministra `P,L,U` con la convención `PA=LU`. Resuelve `Lw=Pb` y `Ux=w` usando tus sustituciones de clase o `scipy.linalg.solve_triangular`. Verifica `PA=LU` y reporta el residuo máximo de `Ax-b`. Explica el intercambio que evita un pivote inicial nulo.

Después ejecuta la rutina de Jacobi suministrada sobre `C(r)=[[1,r],[r,1]]`, para **r=0.2 y r=1.2**, con `b=C(r)(1,2)` y comienzo en cero. Usa el máximo de 200 iteraciones y las tolerancias de la rutina. Compara los historiales de residuo y relaciona convergencia o fallo con la dominancia diagonal. No presentes un agotamiento de iteraciones como solución.

**Entrega:** solución directa con residuo, una gráfica de los dos historiales y conclusión de tres a cinco frases.

**Ampliación no evaluada:** determinante e inversa con LU, r=0.8 o método de potencias para comparar los autovalores de C.

## 4. Resolver un cero y detectar un fallo · Electivo

Completa o adapta tu bisección para `f(x)=x²-2` en `[1,2]`. Compara con **un método a elección: Newton desde 1, secante desde 1 y 2, o Ridder en [1,2]**. Para el método de comparación puedes usar `scipy.optimize.root_scalar`.

Usa tolerancia de posición `1e-10`, residuo `≤1e-10` y máximo 100 iteraciones. La bisección debe controlar la semianchura y el residuo; en la biblioteca verifica el residuo aunque esta informe convergencia. Registra raíz, error respecto a `sqrt(2)`, iteraciones y evaluaciones de f; si usas Newton, cuenta la derivada por separado con `Contador`.

Prueba también la bisección en `[2,3]`: debe rechazar el intervalo e informar el motivo sin detener todo el programa.

**Entrega:** rutina, tabla de los dos métodos, prueba de fallo y conclusión de tres a cinco frases. No se exige una gráfica en este experimento.

**Ampliación no evaluada:** comparar todos los métodos, estudiar el ciclo de `g(x)=2/x`, minimizar por sección áurea o usar el ejemplo suministrado de Newton multidimensional/Broyden.

## 5. Interpolar o ajustar · Electivo

Para `r(x)=1/(1+25x²)` en `[-1,1]`, toma **nueve nodos uniformes y nueve de Chebyshev con extremos**. Usa el interpolador baricéntrico suministrado y compara los dos interpolantes sobre una malla de 401 puntos. Reporta error máximo en esa malla y error en los nodos; grafica las dos curvas con la referencia.

Con las nueve muestras uniformes, ajusta un polinomio de grado cuatro formando la matriz de diseño y las ecuaciones normales. Resuelve con `solve` o tu rutina de pivoteo. Añade su error de entrenamiento y de malla a la tabla. No uses `polyfit` ni `lstsq` en este paso: deben ser visibles las ecuaciones normales.

**Entrega:** sistema de ajuste, tabla comparativa, una figura y conclusión de tres a cinco frases sobre qué representación usarías entre muestras.

**Ampliación no evaluada:** 17 nodos, base monómica, Lagrange o ajuste de una recta.

## Entrega y evaluación

Entrega un solo notebook o script con los tres experimentos elegidos. Las figuras pueden ser paneles de una misma imagen. No se necesita informe separado, portada ni conclusiones de experimentos no elegidos.

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Experimento 1 | **30:** comparación, controles y explicación correctos | **21:** funcional, falta un control o interpretación | **9:** una ejecución útil, comparación insuficiente | **0:** no verificable |
| Primer electivo | **30:** requisitos obligatorios completos y conclusión sustentada | **21:** falta una comprobación o interpretación | **9:** evidencia parcial con errores pendientes | **0:** no verificable |
| Segundo electivo | **30:** requisitos obligatorios completos y conclusión sustentada | **21:** falta una comprobación o interpretación | **9:** evidencia parcial con errores pendientes | **0:** no verificable |
| Reproducibilidad | **10:** ejecución completa y elecciones/procedencia claras | **7:** requiere un ajuste menor | **3:** reconstrucción incompleta | **0:** no se puede ejecutar |

El aporte es `M=R_m/100`, hasta **1 punto**. Las ampliaciones no compensan fallos del núcleo ni son necesarias para el nivel completo. Consulta la [distribución del parcial](../../assessments/README.md#segundo-parcial-talleres-y-exoneración): miércoles 1 punto, viernes 1 y proyecto opcional 3; las tres entregas completas permiten **5.0 y exoneración**.
