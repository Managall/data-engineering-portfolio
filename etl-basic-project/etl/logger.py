# etl/logger.py

import logging

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log"),         # Guarda en archivo
        logging.StreamHandler()                 # Muestra en consola
    ]
)

logger = logging.getLogger(__name__)