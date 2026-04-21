-- Script para criar as tabelas do banco de dados

-- Tabela de questões
CREATE TABLE IF NOT EXISTS questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pergunta TEXT NOT NULL,
    resposta_a TEXT NOT NULL,
    resposta_b TEXT NOT NULL,
    resposta_c TEXT NOT NULL,
    resposta_d TEXT NOT NULL,
    explicacao_a TEXT,
    explicacao_b TEXT,
    explicacao_c TEXT,
    explicacao_d TEXT,
    resposta_certa CHAR(1) NOT NULL CHECK (resposta_certa IN ('A', 'B', 'C', 'D'))
);

-- Tabela de perfis
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL UNIQUE,
    counter_limit INTEGER NULL
);

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nickname TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    profile_id UUID REFERENCES profile(id)
);