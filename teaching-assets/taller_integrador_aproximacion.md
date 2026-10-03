# Viernes: posición de equilibrio de un resorte no lineal

**9 de octubre de 2026 · Trabajo individual · Dos horas · Hasta 1 punto del segundo parcial**

Un laboratorio necesita fijar la posición de montaje de un resorte sometido a una fuerza constante. Construye una aproximación de su energía, encuentra un equilibrio estable y decide si el error de posición cumple la especificación de **0.015 L**. La entrega debe conectar datos, aproximación, solución numérica y recomendación física.

## Modelo y elección del caso

Usa `L=0.02 m`, `E0=0.10 J`, `z=x/L` y la energía idealizada

`U(x)=E0 u(z)`,  `u(z)=sqrt(1+alpha*z²)-1-q*z`,  `-1≤z≤1`.

La fuerza aplicada es `q E0/L`. Elige `alpha` entre 1, 4 y 9, y `q` entre 0.20, 0.30 y 0.40. Registra la elección antes de calcular. Genera nueve muestras con una de estas distribuciones, para `i=0,...,8`:

- Uniforme: `z_i=-1+2i/8`.
- Chebyshev con extremos: `z_i=-cos(i*pi/8)`.

Para evaluar la energía usa `u(z)=alpha*z²/(sqrt(1+alpha*z²)+1)-q*z` y explica su relación con la cancelación numérica. Las muestras son sintéticas: representan un experimento de aproximación de una función conocida.

## Código y herramientas

Escribe tu programa y sus funciones. Debes implementar **eliminación gaussiana con pivoteo parcial, evaluación de Lagrange y bisección**. Puedes incorporar la bisección que adaptaste y las diferencias que utilizaste el jueves, conservando la atribución al libro, y tu eliminación gaussiana desarrollada previamente en clase, indicando su procedencia y verificando que cumplen los controles pedidos. Usa `math` y, si lo deseas, NumPy para organizar datos y Matplotlib para representar resultados; los solucionadores e interpoladores de biblioteca solo pueden emplearse para contrastar tus implementaciones.

Puedes consultar fórmulas y apuntes. Fuera de la reutilización del taller del jueves autorizada arriba, las implementaciones solicitadas deben ser propias; no se admite entregar rutinas copiadas del libro, del repositorio, de tutoriales o de otra persona. Debes poder explicar y modificar el código que presentas.

## Construcción de la aproximación

Con las nueve muestras construye un interpolante de Lagrange y un ajuste `P4(z)=c0+c1*z+...+c4*z⁴`. Para el ajuste forma las ecuaciones normales:

`M_jk=sum(z_i**(j+k))`,  `b_j=sum(u_i*z_i**j)`,  `M c=b`, con `j,k=0,...,4`.

Resuelve el sistema mediante tu eliminación con pivoteo y sustitución hacia atrás. Comprueba tu solucionador con `[[0,2],[1,3]] c=[4,7]`, cuya solución es `[1,2]`: debe intercambiar filas. Informa un pivote numéricamente nulo si impide continuar.

Verifica el residuo máximo de `M c-b` y que el interpolante reproduzca los datos en los nodos. Compara ambas representaciones con u sobre los 40 puntos `z_j=-1+(j+0.5)/20`, para `j=0,...,39`. Reporta sus errores máximos y explica la diferencia entre interpolar y ajustar.

Usa **P4 como modelo operativo**. El objetivo es determinar si una representación de cinco coeficientes permite tomar la decisión de montaje.

## Equilibrio y comprobación física

Evalúa `P4'` con diferencias centrales y Richardson, usando h=0.01. Aplica tu bisección a esa derivada en `[0,0.6]`; comprueba cambio de signo, exige semianchura `≤1e-7` y residuo `≤1e-7`, y limita a 100 iteraciones. Informa raíz, intervalo, residuo y estado de convergencia.

Contrasta el valor de la derivada numérica con la derivada calculada a partir de los coeficientes de P4. Estima la segunda derivada en la raíz con la diferencia central de tres puntos, h=0.01, y compárala con la obtenida de los coeficientes. Su signo permite decidir si el equilibrio es localmente estable. La rigidez es `k_ef=(E0/L²)P4''(z_*)`, en N/m.

Para el modelo ideal, la posición de referencia es

`z_ref=q/sqrt(alpha*(alpha-q²))`.

Comprueba que satisface la ecuación de equilibrio `alpha*z/sqrt(1+alpha*z²)-q=0`. Calcula `L*abs(z_*-z_ref)` y decide si cumple `0.015 L`. La referencia sirve para validar; no sustituye la construcción del ajuste ni la búsqueda de su equilibrio. Un diseño que incumple la especificación puede estar correctamente resuelto: debes identificarlo y justificar la decisión.

## Entrega y sustentación

Entrega un script o notebook ejecutable, una tabla de errores de aproximación, una tabla de equilibrio y rigidez, y una recomendación de **150 a 200 palabras**. Indica parámetros, unidades, posición recomendada, cumplimiento de la especificación y principal fuente de error.

Sustenta por qué usaste pivoteo, qué diferencia hay entre el residuo del sistema y el error de aproximación, y por qué una bisección precisa no garantiza una posición físicamente precisa. En la revisión debes poder señalar el intercambio de filas en tu código y ejecutar un cambio de carga q, explicando el resultado. Las tablas y la sustentación forman parte de la misma entrega.

## Rúbrica

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Aproximación · 20 | **20:** Lagrange propio y P4 correctos, nodos y errores verificados | **14:** ambas aproximaciones válidas con un control pendiente | **6:** una aproximación válida | **0:** sin aproximación verificable |
| Sistema lineal · 20 | **20:** ecuaciones normales, pivoteo propio, prueba y residuo correctos | **14:** solución válida con un diagnóstico pendiente | **6:** algoritmo incompleto o fallo identificado | **0:** no presenta el solucionador propio |
| Equilibrio · 20 | **20:** bisección propia con intervalo, tolerancias y estado comprobados | **14:** raíz válida con un control pendiente | **6:** propuesta de raíz sin acreditar convergencia | **0:** no presenta la búsqueda |
| Validación física · 20 | **20:** derivadas, estabilidad, rigidez y especificación comprobadas con unidades | **14:** decisión válida con una comprobación pendiente | **6:** resultados sin interpretación suficiente | **0:** no evalúa la decisión física |
| Sustentación y ejecución · 20 | **20:** código ejecutable y explicación de algoritmos, errores y cambio de carga | **14:** explicación coherente con una omisión menor | **6:** ejecución o explicación incompleta | **0:** no acredita cómo funciona el código entregado |

El aporte es `V=R_v/100`, hasta **1 punto**. Se aplican las [reglas del segundo parcial](../assessments/README.md#segundo-parcial-talleres-y-exoneración).
