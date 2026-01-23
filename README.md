# Retold Schedule

Telegram‑бот для зручного перегляду розкладу занять та перевірки повітряної тривоги в Україні.

Бот допомагає швидко дізнатися:

* яке зараз заняття
* що буде далі
* розклад на день або тиждень
* чи активна повітряна тривога

## Можливості

* Асинхронний Telegram‑бот на **aiogram 3**
* Робота з розкладом через 
* Перевірка повітряної тривоги через зовнішній API
* Конфігурація через `.env`
* Готовий до запуску в **Docker**

## Стек

* **Python 3.14**
* **aiogram 3**
* **httpx**
* **pydantic / pydantic‑settings**
* **uv** 
* **Docker**

## Налаштування

Створи файл `.env` у корені проєкту:

```env
BOT_TOKEN=your_telegram_bot_token
TELEGRAM_ADMIN_ID=your_telegram_chat_id
ALERT_API_TOKEN=your_api_token (devs.alerts.in.ua)
ALERT_BASE_URL=https://example.com
ALERT_API_REGION_UID=alert_api_region
```

## Запуск локально

```bash
uv sync
uv run python -m src.main
```

## Запуск через Docker

### Збірка образу

```bash
docker-compose up --build -d
```

## Контрибуція

Pull request'и, ідеї та покращення — вітаються.

> Зроблено з ❤️ для зручного та швидкого доступу до розкладу
