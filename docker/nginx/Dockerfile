FROM nginx:alpine

# Копирование конфигурации
COPY nginx.conf /etc/nginx/nginx.conf

# Создание директорий для логов
RUN mkdir -p /var/log/nginx

# Права доступа
RUN chmod 644 /etc/nginx/nginx.conf

# Порты
EXPOSE 80 443

# Команда по умолчанию
CMD ["nginx", "-g", "daemon off;"]
