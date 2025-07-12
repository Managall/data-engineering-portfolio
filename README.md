# 🛠️ Data Engineering Portfolio by Marcio Najarro

![CI](https://github.com/Managall/data-engineering-portfolio/actions/workflows/python-tests.yml/badge.svg)

Bienvenido a mi portafolio de proyectos de Ingeniería de Datos. Aquí encontrarás soluciones prácticas diseñadas para construir experiencia real en ETL, automatización, orquestación, pipelines en la nube y más.

---

## 📁 Proyecto 1: ETL Básico con Python y SQLite

Este proyecto construye un pipeline ETL con enfoque modular y buenas prácticas de desarrollo. Incluye:

- Extracción de datos desde un archivo CSV.
- Transformaciones básicas con pandas.
- Carga a base de datos SQLite.
- Logging estructurado.
- Tests automatizados con pytest.
- Integración continua con GitHub Actions.

---

### 🧰 Tecnologías usadas

- Python 3.11
- pandas
- sqlite3
- pytest
- GitHub Actions
- Logging con `logging`
- CI/CD con workflows `.yml`
- Estructura de proyecto escalable y profesional

---

### 📂 Estructura

```
etl-basic-project/
├── etl/                    # Módulos ETL
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── logger.py
├── tests/                 # Pruebas unitarias
├── data/                  # CSV de entrada y SQLite DB
├── config.py              # Rutas y variables globales
├── main.py                # Pipeline ejecutable
├── requirements.txt
└── .gitignore
```

---

### ⚙️ Cómo ejecutar el pipeline

```bash
# Activar entorno virtual
source venv/bin/activate       # Linux/macOS
.env\Scriptsctivate        # Windows

# Instalar dependencias
pip install -r etl-basic-project/requirements.txt

# Ejecutar el pipeline
cd etl-basic-project
python main.py
```

---

### 🧪 Cómo ejecutar las pruebas

```bash
cd etl-basic-project
pytest
```

Las pruebas también se ejecutan automáticamente en GitHub Actions al hacer push.

---

### 📈 Próximos proyectos

- **Proyecto 2:** Automatización del pipeline ETL con `schedule`, `cron` o `APScheduler`.
- **Proyecto 3:** Pipeline en la nube con AWS S3, Glue y Redshift.
- **Proyecto 4:** Procesamiento en streaming con Kafka o Kinesis.
- **Proyecto 5:** Lakehouse con arquitectura Medallion en Databricks o PySpark.

---

**Marcio Najarro**  
Data Engineer en formación  
📫 marcionajarro@gmail.com | [LinkedIn](www.linkedin.com/in/marcio-andrea-najarro-gallegos-4018b7140)
