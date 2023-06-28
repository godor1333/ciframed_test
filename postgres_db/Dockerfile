# Используем официальный образ PostgreSQL
FROM postgres

# Проброс порта наружу контейнера
EXPOSE 5432

# Установка переменных окружения
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydatabase


# Запуск контейнера
CMD ["postgres"]
