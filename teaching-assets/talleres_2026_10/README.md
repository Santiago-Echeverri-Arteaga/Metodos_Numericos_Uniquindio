# Talleres del segundo parcial

Tres actividades para aplicar los temas vistos en clase. Cada entrega tiene un núcleo obligatorio delimitado; las ampliaciones son de consulta y no se necesitan para obtener la máxima valoración.

| Actividad | Enunciado | Apoyo | Aporte máximo |
| --- | --- | --- | ---: |
| Miércoles 7/10 · Dos horas | [Laboratorio computacional](miercoles_ejercicios.md): experimento 1 y dos electivos | [Plantilla](miercoles_base.py), [rutinas](miercoles_apoyo.py) | 1 punto |
| Viernes 9/10 · Dos horas | [Equilibrio de un resorte](../taller_integrador_aproximacion.md): un ajuste, un interpolante y una decisión | [Plantilla](viernes_base.py) | 1 punto en B |
| Proyecto opcional independiente | [Regresión y posición de operación](proyecto_opcional_regresion.md): OLS, Ridge y Lasso | [Datos y pipelines configurados](regresion_base.py) | 3 puntos |

**Las tres entregas con valoración completa dan 5.0 y exoneración del segundo parcial.** La [regla de evaluación](../../assessments/README.md#segundo-parcial-talleres-y-exoneración) explica los aportes parciales y la alternativa de examen.

## Alcance del trabajo

- El miércoles se entregan tres experimentos, no cinco. Se reutilizan las rutinas de apoyo y se valoran las comparaciones y conclusiones.
- El viernes B exige dos rutinas propias reutilizables: eliminación con pivoteo y bisección. El interpolador está suministrado. La variante A permite librerías y sirve como práctica sin aporte.
- El opcional usa grado 3 fijo, tres pliegues y cinco valores de penalización por familia. No exige implementar sklearn, bootstrap, una segunda búsqueda de raíz ni una ruta numérica adicional.
- No se requieren informes separados. El código de una actividad se puede reutilizar en las siguientes, indicando su procedencia.

El núcleo recorre error numérico, aproximación y ajuste, sistemas lineales, derivación y ceros. Los electivos y ampliaciones permiten profundizar en los demás métodos vistos en clase sin convertirlos en requisitos acumulativos.

## Entorno

Desde la raíz del repositorio y con el entorno virtual activo:

```powershell
python -m pip install -e ".[regresion]"
python teaching-assets/talleres_2026_10/miercoles_base.py
python teaching-assets/talleres_2026_10/viernes_base.py
python teaching-assets/talleres_2026_10/regresion_base.py
```

Las plantillas preparan datos y utilidades; no completan automáticamente la entrega. El viernes B solo usa Python estándar. El miércoles permite NumPy, SciPy y Matplotlib; el opcional añade scikit-learn. Las lecturas necesarias están enlazadas en los enunciados.
