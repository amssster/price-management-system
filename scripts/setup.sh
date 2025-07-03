#!/bin/bash

# Скрипт для быстрой установки системы управления прайс-листами

set -e

echo "🚀 Установка системы управления прайс-листами..."

# Проверка Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker не установлен. Пожалуйста, установите Docker."
    exit 1
fi

# Проверка Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose не установлен. Пожалуйста, установите Docker Compose."
    exit 1
fi

# Копирование файла окружения
if [ ! -f .env ]; then
    echo "📋 Копирование файла окружения..."
    cp .env.example .env
    echo "✅ Файл .env создан. Пожалуйста, отредактируйте его при необходимости."
fi

# Создание необходимых директорий
echo "📁 Создание директорий..."
mkdir -p uploads
mkdir -p logs
mkdir -p static

# Построение и запуск контейнеров
echo "🏗️  Построение и запуск контейнеров..."
docker-compose up -d --build

# Ожидание запуска базы данных
echo "⏳ Ожидание запуска базы данных..."
sleep 30

# Применение миграций
echo "🔄 Применение миграций базы данных..."
docker-compose exec backend alembic upgrade head

# Создание начальных данных
echo "📊 Создание начальных данных..."
docker-compose exec backend python -c "
from app.core.database import SessionLocal
from app.models import *

db = SessionLocal()
# Здесь можно добавить создание начальных данных
db.close()
"

echo "✅ Установка завершена!"
echo ""
echo "🌐 Система доступна по адресам:"
echo "   - Веб-интерфейс: http://localhost"
echo "   - API документация: http://localhost/api/docs"
echo "   - Мониторинг Celery: http://localhost:5555"
echo ""
echo "📚 Дополнительная информация:"
echo "   - Документация: ./docs/"
echo "   - Логи: docker-compose logs -f"
echo "   - Остановка: docker-compose down"
