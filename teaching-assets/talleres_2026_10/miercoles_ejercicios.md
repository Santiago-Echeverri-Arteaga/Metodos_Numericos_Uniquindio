# Miércoles: experimentos de precisión y convergencia

**7 de octubre de 2026 · Trabajo individual · Dos horas · Hasta 1 punto del segundo parcial**

Desarrolla un programa que permita estudiar cómo la aritmética y las decisiones de un algoritmo afectan sus resultados. Resuelve los tres ejercicios y sustenta las conclusiones con mediciones obtenidas por tu código.

## Herramientas y autoría

Escribe tus funciones a partir de las fórmulas y los procedimientos vistos en clase. Puedes usar `math`, NumPy para arreglos y Matplotlib para gráficas. La suma compensada, las diferencias y la bisección deben estar implementadas por ti. Las funciones de biblioteca que resuelven directamente esos cálculos no sustituyen las implementaciones solicitadas.

Puedes consultar apuntes, fórmulas y documentación. No se admite entregar rutinas copiadas del libro, del repositorio, de tutoriales o de otro estudiante. Identifica las fuentes conceptuales utilizadas y conserva el código para explicar su funcionamiento.

## 1. Recuperar información que se pierde al calcular

Para `x=10**(-k)`, con `k=1,...,16`, compara:

`a(x)=sqrt(1+x)-1`,  `b(x)=x/(sqrt(1+x)+1)`.

Antes de ejecutar, explica cuál esperas que conserve mejor la información cuando x sea pequeño. Calcula el error relativo de a usando b como referencia numérica estable, registra el primer x ensayado para el cual a devuelve cero y explica la causa. La referencia también se evalúa con aritmética finita.

Implementa la suma de Kahan y una suma ordinaria mediante un ciclo. Compara ambas sobre `[1e16]+[1.0]*n+[-1e16]`, con `n=10,100,1000`; el valor matemático de cada suma es n. Registra resultado y error absoluto. Explica qué información guarda la compensación y por qué no corrige errores ya presentes en los datos.

**Evidencia:** tabla del barrido, tabla de sumas y una explicación breve de los dos fenómenos.

## 2. Elegir el tamaño de paso con evidencia

Implementa la diferencia central y su extrapolación de Richardson:

`D_h(x)=[f(x+h)-f(x-h)]/(2h)`,

`R_h(x)=[4D_(h/2)(x)-D_h(x)]/3`.

Usa `f(x)=exp(x)`, `x=0` y `h=10**(-k)`, con `k=1,...,10`. La referencia es `f'(0)=1`. Calcula el error absoluto de ambas aproximaciones y representa error contra h en una gráfica logarítmica. Señala los errores que sean cero sin reemplazarlos por números inventados.

Identifica el mejor h ensayado para cada fórmula. Estima el orden observado a partir de los errores de h=0.1 y h=0.01; compara con los órdenes teóricos. Explica por qué hacer h más pequeño puede empeorar el resultado y distingue error del método de error de redondeo.

**Evidencia:** funciones, gráfica y tabla con mejor paso, error y orden observado.

## 3. Encontrar una raíz y reconocer un fallo

Elige `a` entre 2, 3 y 5. Implementa bisección para `f(x)=x²-a` en `[1,3]` y usa `sqrt(a)` únicamente como referencia para comprobar el resultado.

Tu función debe verificar el cambio de signo, admitir una raíz en un extremo, mantener el intervalo que encierra la raíz e informar si convergió. Exige simultáneamente semianchura `≤1e-8` y residuo `≤1e-8`, con máximo 100 iteraciones. Una raíz exacta permite cerrar el intervalo en ese punto.

Entrega raíz, error respecto a la referencia, residuo, intervalo final e iteraciones. Ejecuta además dos controles: el intervalo `[3,4]`, que debe rechazarse, y la búsqueda válida limitada a dos iteraciones, que debe informar que no alcanzó las tolerancias. El programa debe continuar tras registrar esos fallos.

**Evidencia:** implementación, tabla de la búsqueda y resultado de ambos controles. Explica por qué un residuo y un intervalo aportan información diferente.

## Entrega y sustentación

Entrega un script o notebook que ejecute los tres ejercicios de principio a fin. Incluye las tablas, una gráfica y una conclusión de tres a cinco frases por ejercicio.

En la sustentación escrita explica una decisión de implementación en cada ejercicio: la actualización de la compensación, la combinación de pasos de Richardson y la condición de parada de bisección. Durante la revisión debes poder ejecutar tu programa, explicar una función seleccionada y anticipar el efecto de modificar un dato o una tolerancia. Una captura de resultados no sustituye el código ejecutable.

## Rúbrica

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Aritmética y Kahan · 25 | **25:** código propio, comparaciones y errores correctos; explica la pérdida de información | **17:** experimento válido con un diagnóstico incompleto | **7:** ejecución parcial o interpretación insuficiente | **0:** sin experimento verificable |
| Derivación y paso · 25 | **25:** central y Richardson propios, barrido, órdenes y elección de h sustentados | **17:** resultados válidos con una comparación pendiente | **7:** calcula una derivada sin estudiar el paso | **0:** sin implementación verificable |
| Bisección y controles · 30 | **30:** implementación propia, ambas tolerancias y los dos controles de fallo correctos | **21:** raíz válida con un control pendiente | **9:** procedimiento incompleto o convergencia no comprobada | **0:** no implementa la búsqueda |
| Sustentación y reproducibilidad · 20 | **20:** ejecución completa y explicación de decisiones, resultados y cambio de parámetros | **14:** explicación coherente con una omisión menor | **6:** ejecución o explicación incompleta | **0:** no acredita cómo funciona el código entregado |

El aporte es `M=R_m/100`, hasta **1 punto**. Se aplican las [reglas del segundo parcial](../../assessments/README.md#segundo-parcial-talleres-y-exoneración).
