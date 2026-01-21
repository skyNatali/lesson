import pytest
from api.yougile_api import YougileAPI

@pytest.fixture
def api():
    return YougileAPI()

@pytest.fixture
def created_project(api):
    """Создает тестовый проект и возвращает его ID"""
    response = api.create_project("Test Project for Fixture")
    data = response.json()
    
    # Проверяем разные варианты структуры ответа
    if "id" in data:
        project_id = data["id"]
    elif "content" in data and "id" in data["content"]:
        project_id = data["content"]["id"]
    else:
        raise ValueError(f"Не удалось получить ID проекта из ответа: {data}")
    
    yield project_id
    
    # Постараемся удалить проект после теста (если API поддерживает)
    try:
        api.delete_project(project_id)
    except:
        pass  # Игнорируем ошибку удаления

class TestProjectsPositive:
    def test_create_project_success(self, api):
        """Проверяет успешное создание проекта"""
        response = api.create_project("New Project")
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        assert response.status_code == 201
        data = response.json()
        
        # Проверяем, что есть ID
        assert "id" in data
        
        # Проверяем title (если API его возвращает)
        if "title" in data:
            assert data["title"] == "New Project"
        elif "name" in data:  # Иногда API использует "name" вместо "title"
            assert data["name"] == "New Project"
    
    def test_get_project_success(self, api, created_project):
        """Проверяет успешное получение проекта"""
        response = api.get_project(created_project)
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        assert response.status_code == 200
        data = response.json()
        
        # Проверяем, что получили правильный проект
        if "id" in data:
            assert data["id"] == created_project
        elif "content" in data and "id" in data["content"]:
            assert data["content"]["id"] == created_project
    
    def test_update_project_success(self, api, created_project):
        """Проверяет успешное обновление проекта"""
        response = api.update_project(
            created_project, 
            title="Updated Title"
        )
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        assert response.status_code == 200
        data = response.json()
        
        # Проверяем обновленный title
        if "title" in data:
            assert data["title"] == "Updated Title"
        elif "name" in data:
            assert data["name"] == "Updated Title"

class TestProjectsNegative:
    def test_create_project_without_title(self, api):
        """Проверяет создание проекта без title"""
        # Вызываем метод с пустым title (передаем пустую строку)
        response = api.create_project(title="")
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        # API может возвращать 400, 422 или другой код ошибки
        assert response.status_code in [400, 422, 500]
    
    def test_get_nonexistent_project(self, api):
        """Проверяет получение несуществующего проекта"""
        response = api.get_project("non-existent-id-12345")
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        assert response.status_code == 404
    
    def test_update_nonexistent_project(self, api):
        """Проверяет обновление несуществующего проекта"""
        response = api.update_project(
            "non-existent-id-12345",
            title="Some Title"
        )
        print(f"DEBUG: Статус: {response.status_code}, Ответ: {response.text}")
        
        assert response.status_code == 404
