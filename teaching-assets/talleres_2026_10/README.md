# Talleres del segundo parcial

Aplicaremos los temas vistos en clase mediante experimentos computacionales y decisiones sustentadas en resultados numéricos. El trabajo es individual.

| Actividad | Enunciado | Dedicación | Aporte máximo |
| --- | --- | --- | ---: |
| Jueves 8 de octubre | [De las ecuaciones al programa](jueves_ejercicios.md) | Trabajo de clase de dos horas | 1 punto |
| Viernes 9 de octubre | [Equilibrio de un resorte](../taller_integrador_aproximacion.md) | Trabajo de clase de dos horas | 1 punto |
| Proyecto opcional | [Regresión y posición de operación](proyecto_opcional_regresion.md) | Trabajo independiente, aproximadamente cuatro a seis horas | 3 puntos |

**Las tres entregas con valoración completa dan 5.0 y exoneración del segundo parcial.** La [regla de evaluación](../../assessments/README.md#segundo-parcial-talleres-y-exoneración) establece cómo cuentan los aportes parciales y el examen.

## Desarrollo y entrega

El jueves comprende cinco ejercicios de programación a partir del código del libro: acumulación, diferenciación, adaptación de bisección, ensamblaje de un sistema lineal y mínimos cuadrados. El viernes integra interpolación, mínimos cuadrados, eliminación gaussiana, derivación y búsqueda de un equilibrio. El proyecto opcional conecta esos métodos con validación de modelos y regresión lineal, Ridge y Lasso.

Cada entrega consiste en un script o notebook ejecutable con las evidencias y explicaciones indicadas en su enunciado. Las rúbricas incluyen la sustentación: explicar el código, justificar resultados y razonar sobre una modificación de parámetros.

El jueves se reutilizan las rutinas del libro con atribución y se programan los experimentos, las adaptaciones y los controles. Cada enunciado precisa qué puede reutilizarse y qué desarrollo propio exige. En todas las entregas se deben identificar las fuentes y sustentar los cambios y las decisiones; ejecutar código ajeno sin el trabajo solicitado no satisface la actividad.

## Entorno

Con el entorno virtual activo, desde la raíz del repositorio:

```powershell
python -m pip install -e ".[regresion]"
```

El entorno incluye las librerías científicas y scikit-learn. Su disponibilidad no reemplaza las implementaciones propias exigidas en los enunciados.
