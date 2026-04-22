FROM python:3.12-slim

WORKDIR /app

# Impede o Python de gerar arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências do sistema
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    gcc \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

# Instalação de dependências
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Garante permissão do entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

# Inicia servidor Uvicorn carrega app e API na porta 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]