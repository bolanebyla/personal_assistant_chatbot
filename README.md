# Личный чат бот помощник для telegram

Чат бот будет обладать функциями, которые упрощают рутинные задачи

## 🎯 Основные функции

- Получение меню на день из рациона питания
- Управление рационом питания


## 🛠 Технологии

- **Python 3.13+**
- **[Litestar](https://docs.litestar.dev)**
- **[Aiogram](https://docs.aiogram.dev/)** - фреймворк для создания Telegram ботов
- **[Dishka](https://github.com/just-work/dishka)** - контейнер внедрения зависимостей
- **[Pydantic](https://docs.pydantic.dev/)** - валидация данных и настройки
- **[Prometheus](https://prometheus.io/)** - мониторинг метрик (TODO)
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI-сервер
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - работа с БД
- **[Alembic](https://alembic.sqlalchemy.org/)** - управление миграциями
- **[UV](https://github.com/astral-sh/uv)** - менеджер пакетов Python 

## 🏗 Архитектура

Проект построен с использованием следующих архитектурных принципов:

- **Чистая архитектура** - разделение на слои (доменный, прикладной, инфраструктурный)
- **Dependency Injection**
- **Domain-Driven Design**
  - Entities
  - Value objects
  - Domain events
  - Application events
- **REST API**

## 📁 Структура проекта

(TODO)

## 🚀 Запуск проекта

1. Установите зависимости с помощью uv:
```bash
uv pip install .
```

2. Настройте переменные окружения:
```
# Пример конфигурации
TG_BOT_TOKEN=your_bot_token
```

3. Запустите сервер: (TODO)

Для разработки
```bash
```


## 🧪 Тестирование

Запуск тестов (TODO)
```bash
```

## 📊 Мониторинг

Метрики доступны по адресу `/metrics` (Prometheus) (TODO)

## 🔍 Линтеры

В проекте используется [Ruff](https://github.com/astral-sh/ruff)

### Настройка линтера

Конфигурация линтера находится в файле `pyproject.toml` в секции `[tool.ruff]`

### Запуск линтера
```bash
ruff check .
```

Автоматическое исправление проблем
```bash
ruff check --fix .
```

## 🔒 Pre-commit

В проекте настроен pre-commit для автоматической проверки кода перед коммитом. 
Настройки pre-commit находятся в файле `.pre-commit-config.yaml`.

### Установка pre-commit

```bash
pre-commit install
```

После этого pre-commit будет автоматически запускаться перед каждым коммитом.

## 📝 Лицензия
[MIT License](LICENSE)
