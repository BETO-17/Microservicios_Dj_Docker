FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_connection.py .
# Copia opcional de .env si quieres
COPY .env /app/.env

CMD ["python", "test_connection.py"]
