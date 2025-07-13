# etl/logger.py
import os
import logging

# Crear la carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log", mode='a'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
