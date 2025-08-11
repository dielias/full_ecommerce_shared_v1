FROM python:3.12-slim

WORKDIR /app

# Copia o requirements e instala as dependências (incluindo faker)
COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo do locust
COPY locustfile.py .

# Expõe a porta padrão do Locust web UI
EXPOSE 8089

# Comando padrão para rodar o Locust com host padrão (pode ser sobrescrito por variável de ambiente)
CMD ["locust", "-f", "locustfile.py", "--host=http://users:8001"]


