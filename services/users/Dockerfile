FROM python:3.12-slim

WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --default-timeout=100 -r requirements.txt

# Copiar o código da aplicação
COPY shared /app/shared
COPY services/users /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]

