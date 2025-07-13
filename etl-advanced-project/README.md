# 🧪 Proyecto 2: ETL Avanzado con Validación, Tests y Docker

Este proyecto implementa un pipeline ETL avanzado enfocado en validación de datos, testing y despliegue en contenedores.

## 📋 Descripción

- **Extracción:** Carga un archivo CSV (`source_data.csv`) desde `data/`.
- **Validación:** Asegura que el esquema sea correcto, no existan nulos, emails válidos y datos duplicados.
- **Transformación:** Limpia y convierte datos, aplicando mejoras como capitalización de nombres.
- **Carga:** Almacena los datos en una base de datos SQLite (`output.db`).
- **Logging:** Seguimiento completo en `logs/etl.log`.
- **Testing:** Pruebas unitarias con `pytest`.
- **Docker:** Pipeline ejecutable dentro de un contenedor Docker.
- **CI/CD:** Automatización del testeo y build con GitHub Actions.

## 🗃️ Archivos importantes

- `etl/extract.py`: Lógica de extracción.
- `etl/validate.py`: Validaciones estrictas del DataFrame.
- `etl/transform.py`: Limpieza y normalización de datos.
- `etl/load.py`: Persistencia en SQLite.
- `etl/logger.py`: Configuración del logging.
- `main.py`: Orquestación del ETL.
- `Dockerfile`: Contenedor Docker.
- `.github/workflows/`: GitHub Actions.
- `tests/`: Contiene pruebas de cada etapa.

## ▶️ Cómo ejecutar

```bash
python main.py
```

O bien en Docker:

```bash
docker build -t etl-advanced-project .
docker run --rm etl-advanced-project
```

## 🧪 Probar

```bash
pytest
```

## 🧱 Requisitos

```bash
pip install -r requirements.txt
```

## 📁 Estructura de carpetas

```
etl-advanced-project/
├── etl/
├── tests/
├── data/
├── logs/
├── .github/
├── Dockerfile
├── config.py
├── main.py
└── README.md
```

## ✍️ Autor

Marcio Najarro - [marcionajarro@gmail.com](mailto:marcionajarro@gmail.com)
