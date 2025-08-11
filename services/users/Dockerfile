FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

COPY services/shared ./services/shared
COPY services/users ./services/users

CMD ["uvicorn", "services.users.app:app", "--host", "0.0.0.0", "--port", "8001"]




