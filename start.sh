#!/bin/bash

# Iniciar postgres
service postgresql start

# Criar banco (caso não exista)
su postgres -c "psql -c \"CREATE USER postgres WITH PASSWORD 'postgres';\"" || true
su postgres -c "psql -c \"CREATE DATABASE app_db;\"" || true

# Esperar postgres subir
sleep 5

# Rodar migrations (se tiver)
# alembic upgrade head

# Iniciar API
uvicorn src.__main__:app --host 0.0.0.0 --port $PORT