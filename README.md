# Jarvis Bot

Личный ИИ-ассистент в Telegram на базе Groq (Llama 3.3 70B). Бесплатно. Деплой за 5 минут.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/sssviridov1-ops/jarvis-bot)

---

## Что умеет

- Отвечает на вопросы, помогает с задачами — через Groq (бесплатно, 14 400 запросов/день)
- Читает PDF, Excel, текстовые файлы
- Принимает голосовые и видео (транскрипция через Whisper)
- Запускает bash-команды, читает/пишет файлы на сервере
- Ищет в интернете (DuckDuckGo), читает страницы
- Ставит напоминания
- Генерирует карусели для Instagram (тёмный стиль)
- Работает в топиках Telegram-группы
- Поддерживает историю диалога

---

## Быстрый деплой на Render (бесплатно)

### 1. Получи ключи

**Telegram токен** — создай бота через [@BotFather](https://t.me/BotFather):
```
/newbot → дай имя → получи токен вида 123456:ABC-DEF...
```

**Groq API ключ** — бесплатно на [console.groq.com](https://console.groq.com):
```
API Keys → Create API Key → скопируй
```

### 2. Задеплой

Нажми кнопку **Deploy to Render** выше, войди в Render, введи:
- `TELEGRAM_TOKEN` — токен от BotFather
- `GROQ_KEY` — ключ от Groq
- `CHAT_ID` — твой Telegram ID (узнать: [@userinfobot](https://t.me/userinfobot))
- `GROUP_ID` — ID группы (опционально, если используешь топики)

### 3. Настрой UptimeRobot (чтобы не засыпал)

Render Free засыпает после 15 минут без запросов. Чтобы бот работал 24/7:

1. Зарегистрируйся на [uptimerobot.com](https://uptimerobot.com) (бесплатно)
2. Add New Monitor → HTTP(s)
3. URL: `https://твой-сервис.onrender.com`
4. Interval: 5 minutes

---

## Настройка под себя

Отредактируй `CLAUDE.md` — там личный контекст, голос, инструкции для ИИ. Бот читает его при каждом запросе.

Файл `config_render.py` содержит структуру топиков и пути — менять только если нужна кастомная настройка.

---

## Команды в Telegram

| Команда | Описание |
|---------|----------|
| `/статус` | Аптайм, модель, история |
| `/new` | Сбросить историю диалога |
| `/модель [id]` | Сменить модель Groq |
| `/лог` | Лог сегодняшнего дня |
| `/план` | Задачи из лога |
| `/итог` | Итог сессии (сохраняется в лог) |
| `/история [запрос]` | Поиск по истории диалогов |
| `/пост [текст]` | Опубликовать в Telegram-канал |
| `/помощь` | Полная справка |

---

## Обновления

Когда в этом репозитории появляется новый коммит — зайди в Render → твой сервис → **Manual Deploy → Deploy latest commit**.

Или включи Auto-Deploy в настройках сервиса — тогда обновления применяются автоматически.

---

## Стек

- Python 3 · [Groq API](https://groq.com) (OpenAI-compatible) · Llama 3.3 70B
- Telegram Bot API (webhook mode)
- Render.com Free tier
- pdfminer · openpyxl · Pillow
