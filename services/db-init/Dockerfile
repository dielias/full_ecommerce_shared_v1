FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Instalar dependências do sistema e Python
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

COPY services/shared ./services/shared
COPY services/db-init/init_db.py /app/init_db.py

CMD ["python", "-u", "init_db.py"]
