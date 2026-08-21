import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_URL = os.getenv('API_URL')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env!")
if not API_URL:
    raise ValueError("API_URL не найден в .env!")
