import requests
from config import YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID, BASE_URL

print("1. Проверка данных:")
print(f"   Логин: {YOUGILE_LOGIN}")
print(f"   Company ID: {YOUGILE_COMPANY_ID}")

# Пробуем получить токен
auth_data = {
    "login": YOUGILE_LOGIN,
    "password": YOUGILE_PASSWORD,
    "companyId": YOUGILE_COMPANY_ID
}

print("\n2. Получение токена...")
response = requests.post(
    f"{BASE_URL}/api-v2/auth/keys",
    json=auth_data,
    headers={"Content-Type": "application/json"}
)

print(f"   Статус: {response.status_code}")
print(f"   Ответ: {response.text}")

if response.status_code == 201:
    token = response.json()["key"]
    print(f"   Токен: {token[:20]}...")
    
    # Пробуем создать проект с этим токеном
    print("\n3. Пробуем создать проект...")
    project_data = {
        "title": "Test Project"
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    project_response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=project_data,
        headers=headers
    )
    
    print(f"   Статус создания проекта: {project_response.status_code}")
    print(f"   Ответ: {project_response.text}")
else:
    print("   ❌ Не удалось получить токен")
