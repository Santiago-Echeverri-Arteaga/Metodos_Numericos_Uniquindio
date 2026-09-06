# Auditoría y estrategia para los códigos

## Decisión aplicada

No se reescribieron los 63 programas oficiales del libro. Se restauraron exactamente
desde el ZIP suministrado y se conservaron como material de consulta. Las variantes que
ya existían se trasladaron a `examples/class_demos/` para no mezclar originales y
adaptaciones.

Los notebooks aún deben transformarse antes de usarlos como actividades guiadas para
estudiantes.

## Mejoras completadas en las demostraciones

| Archivo | Mejora aplicada | Motivo docente |
|---|---|---|
| `large.py` | Funciones reutilizables y bloque `__main__` | Puede importarse sin imprimir y permite localizar la absorción del incremento |
| `richardsondiff.py` | Funciones para ambas extrapolaciones y tabla de errores | Permite probar órdenes y reutilizar el experimento |
| `suma_kahan.py` | Nombre corregido, documentación e interfaz clara | Evita perpetuar un nombre incorrecto |
| `Ridder.py` | Validación del bracket, estados degenerados y tolerancias absoluta, relativa y residual | Hace explícitos los casos límite |
| `Broyden.py` | Criterios simultáneos de paso y residuo, y detección de estancamiento | Un paso pequeño no se confunde con una raíz |

## Trabajo aún recomendable

| Archivo | Mejora pendiente |
|---|---|
| `finitediff.py` | Separar cálculo, generación de datos y visualización; unificar nombres con el código del libro |
| `Legendre.py` | Documentar el comportamiento en los extremos y separar cálculo de gráfica |
| `Matrices.ipynb` | Añadir explicación, preguntas, norma del residuo y número de condición |
| `MINSTEjemplo.ipynb` | Añadir semilla, instrucciones de instalación y conexión explícita con diferenciación automática |

## Criterio para futuras ediciones

Un código de clase está listo cuando:

1. Puede importarse sin ejecutar cálculos ni abrir gráficas.
2. Tiene una función con entradas y salida claras.
3. Incluye al menos una prueba de una propiedad numérica.
4. Expone un caso en que el método funciona y otro en que falla.
5. Permite regenerar tablas o gráficas mediante un comando documentado.

No es necesario convertir los ejemplos en una biblioteca industrial. Las mejoras deben
hacer visible el razonamiento numérico y facilitar la evaluación, no ocultar los métodos
detrás de demasiada infraestructura.
