FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

# Exponer el puerto para documentación
EXPOSE 8000

# Utilizar una forma más compatible de manejar la variable PORT
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT

# CMD para producción
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]