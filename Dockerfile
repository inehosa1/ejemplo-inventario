# Usa una imagen base de Python
FROM python:3.10-slim

# Evita que Python haga buffering de la salida
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos y luego instálalos
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Expone el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Comando por defecto para iniciar el servidor (modifícalo según tus necesidades)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
