#!/usr/bin/env python3
# Config для Render — читает из переменных окружения
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
GROQ_KEY       = os.environ.get("GROQ_KEY", "")
GROQ_MODEL     = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

CHAT_ID    = os.environ.get("CHAT_ID",    "675453898")
GROUP_ID   = os.environ.get("GROUP_ID",   "-1003723900178")

TOPICS = {
    "📱 Соцсети": 2,
    "🤖 Jarvis":  4,
    "📁 Всё":     7,
    "🐙 GitHub":  9,
    "✅ Задачи":  38,
    "💻 Задачи с компа": 49,
    "КП план": 59,
}

TOPIC_ZADACHI = 38

PROJECT_DIR  = "/tmp/bot"
LOGS_DIR     = f"{PROJECT_DIR}/logs"
BOT_DIR      = PROJECT_DIR
DRAFTS_DIR   = f"{PROJECT_DIR}/drafts"
HISTORY_FILE = f"{PROJECT_DIR}/data/chat_history.json"
TMP_DIR      = "/tmp/bot_media"

BOT_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
