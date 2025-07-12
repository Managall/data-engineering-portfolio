# 🧪 Proyecto 1: ETL Básico con Python

Este proyecto implementa un pipeline ETL simple para practicar los fundamentos de ingeniería de datos con Python.

## 📋 Descripción

- **Extracción:** Lee un archivo CSV (`source_data.csv`) ubicado en `data/`.
- **Transformación:** Aplica transformaciones básicas al DataFrame.
- **Carga:** Guarda los datos en una base SQLite (`output.db`).
- **Logging:** Registra cada paso del proceso con logs informativos.
- **Testing:** Pruebas unitarias con `pytest`.
- **CI/CD:** Validación automática con GitHub Actions.

## 🗃️ Archivos importantes

- `etl/extract.py`: Extracción de datos CSV.
- `etl/transform.py`: Transformaciones con pandas.
- `etl/load.py`: Carga a SQLite.
- `config.py`: Variables globales como rutas.
- `main.py`: Pipeline ejecutable.
- `tests/`: Contiene pruebas unitarias.

## ▶️ Cómo ejecutar

```bash
python main.py
```

## 🧪 Probar

```bash
pytest
```

## 🧱 Requisitos

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 📁 Estructura de carpetas

```
etl-basic-project/
├── etl/
├── tests/
├── data/
├── config.py
├── main.py
└── README.md
```

## ✍️ Autor

Marcio Najarro - [marcionajarro@gmail.com](mailto:marcionajarro@gmail.com)
