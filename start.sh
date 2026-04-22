#!/bin/bash
set -e  # para o script se der erro

echo "🚀 Starting PostgreSQL..."
service postgresql start

echo "⏳ Waiting for PostgreSQL..."
sleep 5

echo "🛠️ Setting up database..."

# Criar user se não existir
su postgres -c "psql -tc \"SELECT 1 FROM pg_roles WHERE rolname='postgres'\" | grep -q 1 || psql -c \"CREATE USER postgres WITH PASSWORD 'postgres';\""

# Criar banco se não existir
su postgres -c "psql -tc \"SELECT 1 FROM pg_database WHERE datname='app_db'\" | grep -q 1 || psql -c \"CREATE DATABASE app_db;\""

echo "✅ Database ready"

# Rodar migrations (se tiver)
# alembic upgrade head

echo "🚀 Starting API..."

exec uvicorn src.__main__:app --host 0.0.0.0 --port $PORT