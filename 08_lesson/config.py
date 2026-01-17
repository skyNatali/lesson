# 08_lesson/config.py
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com"

# Данные для получения токена
YOUGILE_LOGIN = os.getenv("YOUGILE_LOGIN")
YOUGILE_PASSWORD = os.getenv("YOUGILE_PASSWORD")
YOUGILE_COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
YOUGILE_TOKEN = os.getenv("YOUGILE_TOKEN")

def get_auth_token():
    """Получает токен авторизации"""

      # 1. Если есть токен в .env, используем его
    if YOUGILE_TOKEN:
        print("✅ Используем токен из YOUGILE_TOKEN")
        return YOUGILE_TOKEN
    
    import requests
    
    auth_data = {
        "login": YOUGILE_LOGIN,
        "password": YOUGILE_PASSWORD,
        "companyId": YOUGILE_COMPANY_ID
    }
    
    response = requests.post(
        f"{BASE_URL}/api-v2/auth/keys",
        json=auth_data,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 201:
        return response.json()["key"]
    else:
        raise Exception(f"Ошибка получения токена: {response.status_code} - {response.text}")
