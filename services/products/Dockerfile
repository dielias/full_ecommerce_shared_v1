FROM python:3.13.5-slim-bookworm

WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

COPY shared /app/shared
COPY services/products/app.py /app/app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
