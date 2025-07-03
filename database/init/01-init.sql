-- Инициализация базы данных для системы управления прайс-листами

-- Создание базы данных
CREATE DATABASE price_management;

-- Подключение к базе данных
\c price_management;

-- Создание пользователя приложения
CREATE USER app_user WITH PASSWORD 'app_password';

-- Предоставление прав
GRANT ALL PRIVILEGES ON DATABASE price_management TO app_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Создание расширений
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Комментарий
COMMENT ON DATABASE price_management IS 'База данных системы управления прайс-листами';
