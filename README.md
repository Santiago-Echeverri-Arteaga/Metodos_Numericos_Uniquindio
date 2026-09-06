# Métodos Numéricos

Repositorio docente del curso de Métodos Numéricos de la Universidad del Quindío.

**Profesor:** Ph.D. Santiago Echeverri Arteaga

El curso estudia métodos numéricos a partir de su formulación, implementación, análisis
de error y aplicación a problemas físicos. Los programas no se presentan como recetas:
se espera que el estudiante pueda predecir su comportamiento, reconocer sus límites,
validar resultados y justificar la elección de un método.

## Resultados de aprendizaje

Al terminar el curso, el estudiante podrá:

1. Diferenciar errores de representación, redondeo, truncamiento y condicionamiento.
2. Seleccionar un método numérico de acuerdo con exactitud, costo y robustez.
3. Leer, completar, probar y diagnosticar implementaciones numéricas breves.
4. Estimar experimentalmente órdenes de convergencia y fuentes de error.
5. Validar resultados con casos límite, soluciones conocidas o métodos independientes.
6. Interpolar datos, ajustar modelos y analizar residuos.
7. Aproximar integrales y resolver ecuaciones diferenciales evaluando convergencia.
8. Diseñar experimentos computacionales reproducibles.
9. Interpretar resultados dentro de su contexto físico.

## Evaluación

El acta de concertación académica de 2026-2 establece tres parciales en Aulas Virtuales:

| Evaluación | Fecha | Peso |
|---|---:|---:|
| Parcial 1 | 30/09/2026 | 33,4 % |
| Parcial 2 | 28/10/2026 | 33,3 % |
| Parcial 3 | 20/11/2026 | 33,3 % |

La descripción completa está en [assessments/README.md](assessments/README.md) y el
calendario efectivo en [docs/calendario.md](docs/calendario.md).
Las fuentes y decisiones de inclusión están registradas en
[docs/procedencia.md](docs/procedencia.md).

## Material de estudio

- [Presentación general](teaching-assets/aulas_virtuales/00_presentacion_general_metodos_numericos.md)
- [Unidad 1: error numérico](teaching-assets/aulas_virtuales/01_unidad_1_error_numerico.md)
- [Unidad 2: derivación](teaching-assets/aulas_virtuales/02_unidad_2_derivacion_numerica.md)
- [Unidad 3: álgebra lineal](teaching-assets/aulas_virtuales/03_unidad_3_algebra_lineal_numerica.md)
- [Unidad 4: ceros y minimización](teaching-assets/aulas_virtuales/04_unidad_4_ceros_y_minimizacion.md)
- [Unidad 5: aproximación y ajuste](teaching-assets/aulas_virtuales/05_unidad_5_aproximacion_y_ajuste.md)
- [Unidad 6: integración](teaching-assets/aulas_virtuales/06_unidad_6_integracion_numerica.md)
- [Unidad 7: ecuaciones diferenciales](teaching-assets/aulas_virtuales/07_unidad_7_ecuaciones_diferenciales.md)
- [Códigos originales del libro](examples/book_original/README.md)
- [Soluciones desbloqueadas para autoestudio](examples/solutions_self_study/README.md)

Las notas manuscritas vigentes y el libro guía se distribuyen mediante los canales
institucionales; no se versionan completos en Git.

## Organización

```text
.
├── assessments/            # Estructura y criterios de los tres parciales
├── docs/                   # Calendario y mapa entre unidades, notas y códigos
├── examples/
│   ├── book_original/      # Códigos de referencia del libro, sin adaptar
│   ├── class_demos/        # Adaptaciones y demostraciones usadas en clase
│   └── solutions_self_study/ # Soluciones públicas para práctica autónoma
├── notebooks/              # Cuadernos exploratorios
├── references/             # Material complementario y procedencia
├── teaching-assets/        # Presentación, HTML y material histórico
└── tests/                  # Verificaciones automáticas básicas
```

## Instalación

Se recomienda Python 3.11 o posterior y un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebooks]"
```

TensorFlow se mantiene como dependencia opcional porque solamente se utiliza en el
notebook de MNIST:

```powershell
python -m pip install -e ".[ml]"
```

Para verificar el repositorio:

```powershell
python -m pytest
```

## Uso docente

- `examples/book_original/` conserva el material de referencia.
- Las modificaciones para clase deben hacerse en `examples/class_demos/`.
- Los tres parciales se realizan mediante Aulas Virtuales en las fechas concertadas.
- Las actividades calificadas no son ejercicios del libro.
- Los talleres de apoyo no añaden calificaciones al plan concertado.
- Los materiales de terceros conservan sus propios términos de uso; revise
  [references/README.md](references/README.md) antes de redistribuirlos.
