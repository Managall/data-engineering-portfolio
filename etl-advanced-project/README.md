# 🧪 ETL Avanzado con Validación de Datos

Este proyecto es un pipeline ETL avanzado construido con Python que incluye validación de datos, transformación, carga en SQLite y logging personalizado. Es parte de un portafolio de ingeniería de datos.

---

## 📁 Estructura del Proyecto

```
etl-advanced-project/
├── data/
│   ├── source_data.csv       # Archivo fuente de entrada
│   └── output.db             # Base de datos SQLite generada
├── etl/
│   ├── extract.py            # Extracción de datos
│   ├── validate.py           # Validación de esquema y contenido
│   ├── transform.py          # Limpieza y transformación
│   ├── load.py               # Carga en base de datos
│   └── logger.py             # Configuración centralizada de logging
├── config.py                 # Variables globales de configuración
├── main.py                   # Orquestador del pipeline
├── requirements.txt          # Dependencias del entorno
├── venv/                     # Entorno virtual (excluido en Git)
└── etl.log                   # Registro de ejecución (excluido en Git)
```

---

## ⚙️ Funcionalidades

- ✅ Validación de columnas esperadas
- 🧹 Eliminación de nulos y duplicados
- 📧 Validación de formato de correo
- 🔤 Transformación de nombres y correos a minúsculas
- 🗃️ Carga final a SQLite
- 🧾 Logging detallado en `etl.log`

---

## ▶️ Ejecución

1. Activa tu entorno virtual:
   ```bash
   source venv/bin/activate
   ```

2. Ejecuta el pipeline manualmente:
   ```bash
   python main.py
   ```

---

## 🧪 Próximos pasos

- [ ] Añadir tests unitarios con `pytest`
- [ ] Automatizar con `cron` o `APScheduler`
- [ ] Validación con Great Expectations

---

## 📌 Requisitos

- Python 3.11
- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```

---

## 🔒 .gitignore sugerido

```
venv/
__pycache__/
*.pyc
*.log
output.db
```
