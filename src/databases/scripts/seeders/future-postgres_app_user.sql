-- Script para criar/atualizar o usuário de aplicação usado pela API.
-- Rode este arquivo com um usuário administrador (ex.: postgres)
-- já conectado no banco de destino.
--
-- Ajuste a senha abaixo antes de usar em produção.

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_roles
        WHERE rolname = 'app_user'
    ) THEN
        CREATE ROLE app_user
            LOGIN
            PASSWORD 'change_me_app_user_password'
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            NOBYPASSRLS
            INHERIT;
    ELSE
        ALTER ROLE app_user WITH
            LOGIN
            PASSWORD 'change_me_app_user_password'
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            NOBYPASSRLS
            INHERIT;
    END IF;
END $$;

DO $$
BEGIN
    EXECUTE format(
        'GRANT CONNECT ON DATABASE %I TO app_user',
        current_database()
    );
END $$;

GRANT USAGE ON SCHEMA public TO app_user;

GRANT SELECT, INSERT, UPDATE, DELETE
ON ALL TABLES IN SCHEMA public
TO app_user;

GRANT USAGE, SELECT
ON ALL SEQUENCES IN SCHEMA public
TO app_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT USAGE, SELECT ON SEQUENCES TO app_user;
