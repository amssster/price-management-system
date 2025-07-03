FROM node:18-alpine

WORKDIR /app

# Копирование package.json и package-lock.json
COPY package*.json ./

# Установка зависимостей
RUN npm ci --only=production

# Копирование исходного кода
COPY . .

# Создание оптимизированной сборки
RUN npm run build

# Установка serve для статических файлов
RUN npm install -g serve

# Права доступа
RUN chmod -R 755 /app

# Порт
EXPOSE 3000

# Команда по умолчанию
CMD ["serve", "-s", "build", "-l", "3000"]
