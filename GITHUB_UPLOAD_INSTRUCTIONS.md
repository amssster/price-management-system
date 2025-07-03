# Инструкция по загрузке проекта на GitHub

## Шаг 1: Создание репозитория на GitHub

1. Перейдите на https://github.com
2. Нажмите "New repository" (зеленая кнопка)
3. Введите название: `price-management-system`
4. Добавьте описание: `Система управления прайс-листами`
5. Выберите Public или Private
6. НЕ инициализируйте с README (у нас уже есть)
7. Нажмите "Create repository"

## Шаг 2: Инициализация Git в локальной папке

```bash
cd price-management-system
git init
git add .
git commit -m "Initial commit: Price Management System v1.0.0"
```

## Шаг 3: Связывание с GitHub репозиторием

```bash
git remote add origin https://github.com/YOUR_USERNAME/price-management-system.git
git branch -M main
git push -u origin main
```

## Шаг 4: Настройка GitHub Actions (опционально)

Создайте файл `.github/workflows/ci.yml` для автоматической сборки:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  backend-tests:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        cd backend
        pip install -r requirements.txt

    - name: Run tests
      run: |
        cd backend
        pytest

  frontend-tests:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install dependencies
      run: |
        cd frontend
        npm ci

    - name: Run tests
      run: |
        cd frontend
        npm test
```

## Шаг 5: Создание релиза

1. Перейдите в раздел "Releases" на GitHub
2. Нажмите "Create a new release"
3. Введите тег версии: `v1.0.0`
4. Заголовок: `Price Management System v1.0.0`
5. Описание: скопируйте из CHANGELOG.md
6. Загрузите архив `price-management-system-v1.0.0.zip`
7. Нажмите "Publish release"

## Шаг 6: Настройка документации

1. Включите GitHub Pages в настройках репозитория
2. Источник: "Deploy from a branch"
3. Ветка: main
4. Папка: /docs

## Готово! 🎉

Ваш проект теперь доступен по адресу:
https://github.com/YOUR_USERNAME/price-management-system

Для клонирования:
```bash
git clone https://github.com/YOUR_USERNAME/price-management-system.git
```
