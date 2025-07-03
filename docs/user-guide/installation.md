# Руководство по установке

Это руководство поможет вам установить и настроить систему управления прайс-листами.

## Системные требования

### Минимальные требования
- ОС: Linux, macOS, Windows 10+
- RAM: 4 GB
- Дисковое пространство: 10 GB
- Docker: 20.10+
- Docker Compose: 2.0+

### Рекомендуемые требования
- RAM: 8 GB или больше
- Дисковое пространство: 50 GB или больше
- SSD диск для лучшей производительности

## Быстрая установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/price-management-system.git
cd price-management-system
```

### 2. Настройка окружения

```bash
# Копирование файла окружения
cp .env.example .env

# Отредактируйте .env файл
nano .env
```

### 3. Запуск системы

```bash
# Автоматическая установка
./scripts/setup.sh

# Или вручную
docker-compose up -d --build
```

### 4. Проверка установки

Откройте браузер и перейдите по адресу:
- Веб-интерфейс: http://localhost
- API документация: http://localhost/api/docs

## Детальная установка

### Установка Docker

#### Ubuntu/Debian
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### CentOS/RHEL
```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
```

#### macOS
Скачайте Docker Desktop с официального сайта: https://www.docker.com/products/docker-desktop

#### Windows
Скачайте Docker Desktop с официального сайта: https://www.docker.com/products/docker-desktop

### Настройка базы данных

По умолчанию используется PostgreSQL в Docker контейнере. Для использования внешней базы данных:

```bash
# В .env файле
DATABASE_URL=postgresql://username:password@host:port/database_name
```

### Настройка Redis

По умолчанию используется Redis в Docker контейнере. Для использования внешнего Redis:

```bash
# В .env файле
REDIS_URL=redis://host:port
CELERY_BROKER_URL=redis://host:port
CELERY_RESULT_BACKEND=redis://host:port
```

## Развертывание в production

### 1. Настройка переменных окружения

```bash
cp config/production/.env.production .env
# Отредактируйте .env файл с production настройками
```

### 2. Использование production конфигурации

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### 3. Настройка SSL

```bash
# Добавьте SSL сертификаты в docker/nginx/
# Обновите nginx.conf для HTTPS
```

## Обновление системы

```bash
# Остановка системы
docker-compose down

# Обновление кода
git pull origin main

# Пересборка и запуск
docker-compose up -d --build

# Применение миграций
docker-compose exec backend alembic upgrade head
```

## Резервное копирование

```bash
# Создание резервной копии
./scripts/backup.sh

# Восстановление из резервной копии
./scripts/restore.sh backup_file.sql
```

## Устранение неполадок

### Проблемы с правами доступа

```bash
# Исправление прав доступа
sudo chown -R $USER:$USER ./uploads
sudo chown -R $USER:$USER ./logs
```

### Проблемы с портами

```bash
# Проверка занятых портов
netstat -tuln | grep -E ':(80|3000|5432|6379|8000)'

# Изменение портов в docker-compose.yml
```

### Проблемы с памятью

```bash
# Увеличение памяти для Docker
# Docker Desktop -> Settings -> Resources -> Memory
```

## Дополнительные настройки

### Мониторинг

```bash
# Просмотр логов
docker-compose logs -f

# Мониторинг ресурсов
docker stats
```

### Масштабирование

```bash
# Увеличение количества worker'ов
docker-compose up -d --scale celery-worker=4
```

Для получения дополнительной помощи обратитесь к [документации по устранению неполадок](troubleshooting.md).
