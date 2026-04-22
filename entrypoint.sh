#!/bin/sh
set -e

DB_HOST="db"
DB_PORT="5432"

echo "Aguardando banco de dados em $DB_HOST:$DB_PORT..."

export PGPASSWORD="$POSTGRES_PASSWORD"

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$POSTGRES_USER"; do
  echo "Aguardando disponíbilidade do banco..."
  sleep 2
done

echo "Conexão estabelecida - Banco disponível!"

exec "$@"