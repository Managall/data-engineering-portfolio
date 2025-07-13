# Usa una imagen base con Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
 && pytest > /app/test_results.txt || true

# Comando por defecto al ejecutar el contenedor
CMD ["python", "main.py"]
