import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия драйвера."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет корректность вычислений калькулятора с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser):
    """
    Тест работы калькулятора с задержкой вычислений.
    
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Выполнить операцию 7 + 8
    4. Проверить результат (должен быть 15)
    """
    with allure.step("Создать объект страницы калькулятора"):
        calculator_page = CalculatorPage(browser)
    
    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()
    
    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)
    
    with allure.step("Нажать кнопки: 7, +, 8, ="):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
    
    with allure.step("Получить и проверить результат"):
        result = calculator_page.get_result()
        with allure.step(f"Проверить что результат равен 15 (фактический: {result})"):
            assert result == "15", f"Ожидалось 15, получено {result}"


@allure.title("Альтернативная проверка калькулятора")
@allure.description("Тест использует метод perform_calculation для выполнения операций")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator_alternative(browser):
    """Альтернативный тест с использованием метода perform_calculation."""
    with allure.step("Создать объект страницы калькулятора"):
        calculator_page = CalculatorPage(browser)
    
    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()
    
    with allure.step("Выполнить операцию 7 + 8 с задержкой 45 секунд"):
        calculator_page.perform_calculation(
            delay=45,
            sequence=["7", "+", "8", "="]
        )
    
    with allure.step("Проверить результат"):
        result = calculator_page.get_result()
        with allure.step(f"Проверить что результат равен 15 (фактический: {result})"):
            assert result == "15"
