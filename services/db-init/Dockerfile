FROM python:3.13.5-slim-bookworm

WORKDIR /app

# Copia o requirements.txt e instala dependências primeiro
COPY requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

# Agora copia os códigos
COPY shared /app/shared
COPY services/db-init/init_db.py /app/init_db.py

CMD ["python", "init_db.py"]
