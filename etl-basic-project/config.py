# Config.py

import os

# Directorio base (donde se ubica este archivo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas absolutas construidas desde BASE_DIR
SOURCE_CSV_PATH = os.path.join(BASE_DIR, 'data', 'source_data.csv')
SQLITE_DB_PATH = os.path.join(BASE_DIR, 'data', 'output.db')

# Nombre de la tabla
SQLITE_DB_NAME = "health_data"
