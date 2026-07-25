from urllib import response

import requests
from flask import current_app

def get_quote():
    url = current_app.config['URL']
    print(f"URL: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:        
        response = requests.get(url, headers=headers)
        print(f"СТАТУС ОТВЕТА API: {response.status_code}")
        print(f"ТЕЛО ОТВЕТА API: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            print("API вернул ошибку, цитата не получена.")
            return None
    except Exception as e:
        print(f"Сетевая ошибка при запросе: {e}")
        return None 