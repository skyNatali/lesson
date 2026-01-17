Инструкция для наставника:
Шаги для запуска тестов:
Клонируйте репозиторий и перейдите в ветку lesson8:

bash
git clone <репозиторий>
git checkout lesson8
cd 08_lesson
Создайте виртуальное окружение и установите зависимости:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

pip install -r requirements.txt
Создайте файл .env на основе .env.example с вашими данными:

bash
cp .env.example .env
Затем отредактируйте .env:

text
YOUGILE_LOGIN=email_наставника@mail.ru
YOUGILE_PASSWORD=пароль_наставника
YOUGILE_COMPANY_ID=company_id_наставника
Получите токен (если нужно):

Запустите тесты, они автоматически получат токен

Или получите токен вручную:

bash
python -c "from config import YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID; import requests; auth_data={'login':YOUGILE_LOGIN,'password':YOUGILE_PASSWORD,'companyId':YOUGILE_COMPANY_ID}; r=requests.post('https://ru.yougile.com/api-v2/auth/keys',json=auth_data,headers={'Content-Type':'application/json'}); print(r.json()['key'] if r.status_code==201 else r.text)"
Добавьте полученный токен в .env как YOUGILE_TOKEN

Запустите тесты:

bash
pytest tests/ -v
# или из корня проекта:
pytest 08_lesson -v
