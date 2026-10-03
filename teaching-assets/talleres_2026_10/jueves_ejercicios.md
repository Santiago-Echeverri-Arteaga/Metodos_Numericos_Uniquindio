# Jueves: laboratorio de diagnóstico numérico

**8 de octubre de 2026 · Trabajo individual · Dos horas · Hasta 1 punto del segundo parcial**

Investiga cuándo un cálculo aparentemente correcto pierde precisión o produce una respuesta que no está justificada. El trabajo comprende tres experimentos sobre los temas vistos en clase: debes anticipar resultados, programar comparaciones, interpretar evidencia y adaptar una rutina para que sus resultados sean verificables.

## Punto de partida y herramientas

Parte de las implementaciones del libro disponibles en el repositorio:

- [Suma de Kahan](../../examples/book_original/kahansum.py).
- [Diferencias finitas](../../examples/book_original/finitediff.py) y [extrapolación de Richardson](../../examples/book_original/richardsondiff.py).
- [Bisección](../../examples/book_original/bisection.py).

Puedes importarlas o incorporar las funciones necesarias conservando la atribución. **No debes reescribir estos algoritmos desde cero.** Lee su funcionamiento y construye sobre ellos: el trabajo propio son los experimentos, las adaptaciones, las pruebas y las conclusiones. Señala qué código procede del libro y qué cambiaste. Trabaja en tu archivo de entrega, sin modificar los originales del repositorio.

Puedes usar `math`, NumPy y Matplotlib para organizar datos, calcular referencias y representar resultados. Usa un ciclo de acumulación para la suma ordinaria: algunas funciones de suma de biblioteca incorporan estrategias que alterarían la comparación. No se entrega una plantilla resuelta; organiza tu programa en funciones y conserva los resultados de cada experimento.

## 1. Auditar una suma: estabilidad y orden de los datos

Una aplicación acumula incrementos pequeños junto a valores mucho mayores. Antes de calcular, predice qué casos deberían ser sensibles al orden y si esperas que Kahan recupere siempre el resultado matemático.

Construye estas tres secuencias:

| Caso | Datos | Suma matemática |
| --- | --- | ---: |
| A | `[1e16] + [1.0]*1000 + [-1e16]` | 1000 |
| B | `[1e16, 1.0, -1e16]` | 1 |
| C | Mil repeticiones de `[1e16, 1.0, -1e16]` | 1000 |

Programa un experimento que aplique suma ordinaria y Kahan a cada secuencia en su orden original y ordenada por magnitud creciente. Conserva todos los datos; usa una ordenación estable para los empates. Registra resultado y error absoluto: la tabla debe permitir comparar los doce resultados sin inspeccionar manualmente cada ejecución.

Localiza un caso en el que Kahan mejore el resultado y otro en el que no recupere la suma matemática. Para el caso B original registra, paso a paso, el acumulador y la compensación de la rutina del libro. Relaciona esa traza con la limitación observada. Distingue el efecto de cambiar el algoritmo del efecto de cambiar el orden.

Cierra el diagnóstico con una segunda fuente de pérdida de información: evalúa `sqrt(1+x)-1` y `x/(sqrt(1+x)+1)` para `x=10**(-k)`, con `k=4,8,12,16`. Usa la segunda expresión como referencia numérica estable, calcula el error relativo de la primera y explica por qué aplicar Kahan después de obtener un término redondeado a cero no recuperaría ese término.

**Evidencia:** tabla de sumas, traza de tres pasos, tabla de cancelación y una recomendación breve sobre cómo tratarías estos datos. La referencia estable también se calcula en aritmética finita.

## 2. Elegir un paso cuando la evaluación tiene resolución limitada

Elige `a` entre 1, 2 y 3. Trabaja con `f(x)=exp(a*x)` en `x0=0.4`, cuya derivada de referencia es `a*exp(a*x0)`. Simula además una lectura con resolución limitada mediante `f_medida(x)=round(f(x),6)`. La referencia de interés sigue siendo la derivada de la función suave f, no la de la función redondeada.

Adapta los ejemplos del libro para barrer `h=10**(-k)`, con `k=1,...,10`, y comparar diferencia hacia adelante, diferencia central y Richardson aplicado a la central. Haz el mismo barrido con f y con f_medida. En `calc_cd` del libro, h es la separación total entre los dos puntos: se evalúa en `x±h/2`. Conserva esa convención al aplicar Richardson.

Genera una figura con dos paneles —evaluación original y lectura redondeada—, mostrando las tres curvas de error absoluto frente a h en escala logarítmica. Identifica los errores nulos sin inventar valores para representarlos. Resume en una tabla el mejor h ensayado y su error para cada una de las seis combinaciones.

Con la evaluación original estima el orden observado de los tres métodos usando h=0.1 y h=0.01. Explica cualquier desviación respecto al orden esperado. Para la lectura redondeada elige un método y un paso a partir de la evidencia; después comprueba esa elección en `x1=0.7`, sin volver a seleccionar h. Compara allí su error con el del mismo método usando h=1e-10.

**Evidencia:** figura, tabla de pasos y errores, órdenes observados y comprobación en x1. Justifica si un método de mayor orden o un paso menor garantiza mejores resultados cuando cambia la calidad de las evaluaciones.

## 3. Convertir una rutina de bisección en un resultado confiable

Ejecuta la bisección original del libro en estos casos. Captura el resultado o la excepción para que el experimento continúe y contrasta lo observado con lo que matemáticamente debería ocurrir:

| Función | Intervalo | Propiedad que debes comprobar |
| --- | --- | --- |
| `x**2-2` | `[1,2]` | Raíz interior, referencia `sqrt(2)` |
| `x-1` | `[1,2]` | Raíz en un extremo |
| `x` | `[-1,1]` | Raíz exactamente en el punto medio |
| `x**2+1` | `[-1,1]` | No existe raíz real |

A partir de ese diagnóstico, **modifica la rutina existente** para validar los extremos, tratar raíces exactas, rechazar intervalos sin cambio de signo y devolver raíz, residuo, intervalo final, iteraciones y estado de convergencia. Conserva la lógica de bisección y explica los cambios. Sustituye la parada relativa del ejemplo por semianchura del intervalo `≤1e-8`, con máximo 100 iteraciones; una raíz exacta permite cerrar el intervalo en ese punto. Reporta el residuo como un diagnóstico independiente.

Verifica tu adaptación con los cuatro casos y repite el primero limitándolo a dos iteraciones: debe informar que no alcanzó la tolerancia. Para los intervalos válidos comprueba además que las semianchuras disminuyen y que la raíz de referencia queda dentro del intervalo final.

Finalmente, aplica la adaptación a `g(x)=s*(x**2-2)` en `[1,2]`, con `s=1e-12,1,1e12`. Compara error en la raíz, residuo e iteraciones. Calcula también el residuo de las tres funciones en x=1.5: ¿qué aceptarías incorrectamente si solo exigieras un residuo menor que 1e-8? Justifica por qué cambiar la escala de una función puede cambiar su residuo sin cambiar sus ceros.

**Evidencia:** tabla de diagnóstico original/adaptado, código con cambios identificados, controles de convergencia y tabla del experimento de escala.

## Entrega y sustentación

Entrega un script o notebook ejecutable con los tres experimentos, sus tablas, la figura y una conclusión de tres a cinco frases por experimento. Las explicaciones van junto a los resultados; no se requiere un informe separado. Identifica las funciones reutilizadas y las modificaciones propias.

En la revisión debes poder explicar la traza de Kahan, defender la elección del paso y mostrar qué control agregaste a bisección y por qué. Debes poder anticipar el efecto de cambiar un parámetro y verificarlo ejecutando tu programa. Ejecutar los ejemplos originales sin desarrollar los experimentos y el diagnóstico no satisface la entrega.

## Rúbrica

| Criterio | Completo | Parcial | Inicial | Sin evidencia |
| --- | --- | --- | --- | --- |
| Estabilidad y orden de suma · 25 | **25:** compara los doce resultados, explica la traza y conecta cancelación con pérdida de información | **17:** experimentos correctos con un diagnóstico pendiente | **7:** resultados aislados sin contraste suficiente | **0:** sin experimento verificable |
| Derivación con resolución limitada · 30 | **30:** seis barridos, órdenes, elección razonada y comprobación en x1 | **21:** comparación válida con una comprobación pendiente | **9:** calcula derivadas sin justificar el paso | **0:** sin comparación verificable |
| Diagnóstico y adaptación de bisección · 30 | **30:** identifica fallos, adapta la rutina, verifica los controles y explica el efecto de escala | **21:** adaptación válida con un control o diagnóstico pendiente | **9:** cambios sin verificar los casos requeridos | **0:** sin adaptación ni diagnóstico |
| Sustentación y reproducibilidad · 15 | **15:** ejecución completa, atribución clara y defensa de cambios y decisiones | **10:** explicación coherente con una omisión menor | **4:** ejecución o explicación incompleta | **0:** no acredita cómo funciona la entrega |

El aporte es `J=R_j/100`, hasta **1 punto**. Se aplican las [reglas del segundo parcial](../../assessments/README.md#segundo-parcial-talleres-y-exoneración).
