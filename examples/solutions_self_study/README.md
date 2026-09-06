# Soluciones para autoestudio

Soluciones que el material suministrado por el autor identifica explícitamente como
desbloqueadas y disponibles para todos los lectores. Se publican como apoyo para quien
desee resolver ejercicios por cuenta propia; no corresponden a preguntas de los
parciales del curso.

| Capítulo | Problemas con solución |
|---:|---|
| 1 | 3, 10 |
| 2 | 5, 14, 19 |
| 3 | 5, 10 |
| 4 | 6, 24, 49 |
| 5 | 11, 15, 18, 21, 25 |
| 6 | 5, 13, 22, 46 |
| 7 | 2, 21, 25, 62 |
| 8 | 7, 28, 29, 34 |

## Uso recomendado

1. Intentar primero el problema sin consultar la solución.
2. Comparar el planteamiento y las decisiones algorítmicas, no solo la salida.
3. Ejecutar el código con otros parámetros y diseñar un caso de validación.
4. Explicar por qué converge y en qué condiciones podría fallar.

Los archivos conservan la atribución original a Alex Gezerlis y a *Numerical Methods in
Physics with Python*, segunda edición, Cambridge University Press, 2023.

## Ejecución

Algunas soluciones importan funciones de los códigos guía. Desde la raíz del
repositorio, en PowerShell, use:

```powershell
$env:PYTHONPATH = "examples/book_original"
python examples/solutions_self_study/prob_ch5_21.py
```

Cambie el nombre del archivo por la solución que quiera estudiar. Las dependencias
científicas se instalan con `python -m pip install -e .`.
