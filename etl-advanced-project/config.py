# config.py

# Rutas de archivos
SOURCE_CSV_DATA = "data/source_data.csv"
SQLITE_DB_PATH = "data/output.db"

# Nombre de la tabla en la base de datos
SQLITE_DB_NAME = "users"

# Esquema esperado para validación
EXPECTED_COLUMNS = ["id", "nombre", "edad", "email", "suscrito"]