import requests
import json

# Ваши реальные данные для входа в Yougile
LOGIN = "nanalu1@mail.ru"
PASSWORD = "Nana060606@!"

def get_company_id():
    """Получает список компаний и их ID"""
    auth_data = {
        "login": LOGIN,
        "password": PASSWORD
    }
    
    response = requests.post(
        "https://ru.yougile.com/api-v2/auth/companies",
        json=auth_data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Статус код: {response.status_code}")
    print(f"Ответ сервера: {response.text}")
    
    if response.status_code == 200:
        try:
            # Парсим JSON ответ
            response_data = response.json()
            
            # Извлекаем список компаний из поля "content"
            if "content" in response_data and response_data["content"]:
                companies = response_data["content"]
                print("\n" + "="*50)
                print("НАЙДЕНЫ КОМПАНИИ:")
                for company in companies:
                    print(f"  Название: {company.get('name', 'Нет названия')}")
                    print(f"  ID: {company.get('id')}")
                    print(f"  Админ: {company.get('isAdmin', False)}")
                    print("  ---")
                
                # Берем ID первой компании
                company_id = companies[0]["id"]
                print(f"\n✅ ВАШ ID КОМПАНИИ: {company_id}")
                print("="*50)
                
                # Показываем, что нужно сделать дальше
                print("\n📋 ДЛЯ КОПИРОВАНИЯ В .env ФАЙЛ:")
                print(f"YOUGILE_COMPANY_ID={company_id}")
                
                return company_id
            else:
                print("❌ Поле 'content' пустое или отсутствует в ответе")
                print(f"Структура ответа: {json.dumps(response_data, indent=2)}")
                return None
        except json.JSONDecodeError:
            print("❌ Ошибка декодирования JSON")
            return None
    else:
        print(f"❌ Ошибка запроса: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    company_id = get_company_id()
    if company_id:
        print(f"\n🎉 Успешно! ID компании: {company_id}")
    else:
        print("\n⚠️ Не удалось получить ID компании.")
