# etl/logger.py
import os
import logging

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar logging global
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log", mode='a'),
        logging.StreamHandler()
    ]
)

# Instancia específica de logger para el módulo
logger = logging.getLogger(__name__)
