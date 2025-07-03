# Система управления прайс-листами

Полнофункциональная система для автоматизации работы с прайс-листами поставщиков, управления товарами и ценообразованием.

## 🚀 Возможности

- **Импорт данных**: Поддержка Excel, CSV, XML, Google Sheets
- **Автоматизация**: Планировщик задач и автоматические обновления
- **Ценообразование**: Гибкие формулы наценок и округления
- **Управление каталогом**: Массовое редактирование товаров
- **Аналитика**: Детальные отчеты и мониторинг
- **API**: REST API для интеграции с внешними системами

## 🛠 Технологии

- **Backend**: FastAPI, Python 3.11, PostgreSQL, Redis
- **Frontend**: React 18, TypeScript, Tailwind CSS
- **Инфраструктура**: Docker, Nginx, Celery
- **Мониторинг**: Flower, Prometheus, Grafana

## 📦 Быстрый старт

### Установка с Docker

```bash
# Клонирование репозитория
git clone https://github.com/your-username/price-management-system.git
cd price-management-system

# Настройка окружения
cp .env.example .env
# Отредактируйте .env файл

# Запуск всех сервисов
docker-compose up -d

# Инициализация базы данных
docker-compose exec backend alembic upgrade head
```

### Доступ к системе

- **Веб-интерфейс**: http://localhost
- **API документация**: http://localhost/api/docs
- **Мониторинг Celery**: http://localhost:5555
- **Админ панель**: http://localhost/admin

## 🏗 Архитектура

```
price-management-system/
├── backend/           # FastAPI приложение
├── frontend/          # React приложение
├── database/          # Схемы и миграции БД
├── docker/            # Docker конфигурации
├── docs/              # Документация
└── scripts/           # Скрипты для развертывания
```

## 📖 Документация

- [Руководство по установке](docs/user-guide/installation.md)
- [Руководство пользователя](docs/user-guide/user-manual.md)
- [API документация](docs/api/README.md)
- [Развертывание в production](docs/deployment/production-guide.md)

## 🤝 Вклад в проект

Смотрите [CONTRIBUTING.md](CONTRIBUTING.md) для информации о том, как внести вклад в проект.

## 📄 Лицензия

Этот проект лицензирован под MIT License - смотрите [LICENSE](LICENSE) файл для деталей.

## 🆘 Поддержка

- [Troubleshooting](docs/user-guide/troubleshooting.md)
- [Issues](https://github.com/your-username/price-management-system/issues)
- [Discussions](https://github.com/your-username/price-management-system/discussions)
