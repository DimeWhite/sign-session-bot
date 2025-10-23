# 📌 Telegram Bot with Google Sheets Integration

Асинхронный Telegram бот для работы с пользователями и Google Sheets.

Позволяет:

- Принимать геолокацию пользователей
- Отслеживать сессии
- Сохранять комментарии
- Работать с Google Sheets через сервисный аккаунт
- Работать с Dadata API для обратного геокодирования
- Полностью асинхронная обработка сообщений через aiogram 3.x

## ⚡ Установка и запуск

1. Клонируем проект

```bash
git clone <repo-url>
cd project
```

2. Копируем .env

```
cp .env.example .env
```

3.  Собираем через Docker

```bash
docker-compose build
```

3. Запускаем контейнер

```
   docker-compose up -d
```

## Технологии

- Python 3.12.10
- aiogram 3.x
- Google Sheets API (gspread + google-auth)
- Dadata API для обратного геокодирования
- Pydantic-settings для конфигурации
- Docker / Docker Compose
