import requests
from config import BASE_URL, get_auth_token

class YougileAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.token = get_auth_token()  # Получаем токен при создании
        self._update_headers()
    
    def _update_headers(self):
        """Обновляет заголовки с текущим токеном"""
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def _refresh_token_if_needed(self):
        """Обновляет токен, если истек"""
        pass
    
    def _make_request(self, method, url, **kwargs):
        """Универсальный метод для выполнения запросов с обработкой ошибок"""
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            
            # Если токен истек, обновляем его и повторяем запрос
            if response.status_code == 401:
                # Здесь можно добавить логику обновления токена
                pass
                
            return response
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            raise
    
    def create_project(self, title, description=None):
        """Создает проект"""
        url = f"{self.base_url}/api-v2/projects"
        data = {"title": title}
        
        response = requests.post(url, json=data, headers=self.headers)
        
        # Добавьте отладку для понимания структуры ответа
        print(f"DEBUG create_project: status={response.status_code}, response={response.text}")
        
        return response
    
    def get_project(self, project_id):
        """Получает проект по ID"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        
        print(f"DEBUG get_project: status={response.status_code}, response={response.text}")
        return response
    
    def update_project(self, project_id, title=None, description=None):
        """Обновляет проект"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        data = {}
        if title:
            data["title"] = title
        
        response = requests.put(url, json=data, headers=self.headers)
        
        print(f"DEBUG update_project: status={response.status_code}, response={response.text}")
        return response
    
    def delete_project(self, project_id):
        """Удаляет проект (если поддерживается API)"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        return response
