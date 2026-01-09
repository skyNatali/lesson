# Домашнее задание 9: SQLAlchemy и PostgreSQL

## Описание
Тесты для работы с базой данных PostgreSQL с использованием SQLAlchemy ORM.

## Структура проекта
- `config.py` - конфигурация подключения к БД
- `models.py` - модели SQLAlchemy (Student, Course, Enrollment)
- `test_database.py` - 7 тестов (3 обязательных + 4 дополнительных)
- `requirements.txt` - зависимости
- `.env.example` - шаблон для переменных окружения

## Установка и запуск

### 1. Настройка базы данных
```bash
# Подключитесь к PostgreSQL и создайте базу данных
createdb mydatabase

# Или через psql
psql -U postgres
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
