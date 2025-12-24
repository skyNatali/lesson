import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    # 1. Создаем объект страницы
    calculator_page = CalculatorPage(browser)
    
    # 2. Открываем страницу калькулятора
    calculator_page.open()
    
    # 3. Вводим задержку 45 секунд
    calculator_page.set_delay(45)
    
    # 4. Нажимаем кнопки: 7, +, 8, =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")
    
    # 5. Проверяем результат через 45 секунд
    result = calculator_page.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"


# Альтернативный вариант с использованием метода perform_calculation
def test_slow_calculator_alternative(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.open()
    
    # Используем метод для выполнения последовательности операций
    calculator_page.perform_calculation(
        delay=45,
        sequence=["7", "+", "8", "="]
    )
    
    result = calculator_page.get_result()
    assert result == "15"
