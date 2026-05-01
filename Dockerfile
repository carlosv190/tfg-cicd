# Imagen base: Python 3.12 en su versión ligera
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias y las instalamos
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación
COPY app/app.py .

# Puerto que expone el contenedor
EXPOSE 5000

# Comando que se ejecuta al arrancar el contenedor
CMD ["python", "app.py"]
