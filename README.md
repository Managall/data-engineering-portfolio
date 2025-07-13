# Portafolio de Proyectos de Ingeniería de Datos

Este repositorio contiene una colección de proyectos diseñados para demostrar habilidades clave de un Ingeniero de Datos. Cada proyecto sigue buenas prácticas de ingeniería, incluyendo validación de datos, pruebas automatizadas, ejecución con Docker y despliegue continuo.

## Proyectos

### 1. ETL Básico Automatizado (`etl-basic-project`)
Un pipeline ETL simple que:
- Extrae datos desde un archivo CSV.
- Transforma y limpia los datos.
- Carga los datos en una base de datos SQLite.
- Se ejecuta automáticamente usando `cron` y `schedule`.
- Incluye logging.

### 2. ETL Avanzado con Validación, Docker y CI/CD (`etl-advanced-project`)
Un pipeline más robusto que:
- Realiza validaciones detalladas con `Great Expectations`.
- Incluye pruebas unitarias con `pytest`.
- Está dockerizado para facilitar su despliegue.
- Se ejecuta automáticamente desde GitHub Actions.
