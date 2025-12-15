import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Простая инициализация
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    # 1. Открыть страницу калькулятора
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Установить задержку 45 секунд
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажать кнопки 7 + 8 =
    browser.find_element(
        By.CSS_SELECTOR, ".keys .btn-outline-primary:nth-child(1)").click()
    browser.find_element(
        By.CSS_SELECTOR, ".keys .btn-outline-success:nth-child(4)").click()
    browser.find_element(
        By.CSS_SELECTOR, ".keys .btn-outline-primary:nth-child(2)").click()
    browser.find_element(
        By.CSS_SELECTOR, ".keys .btn-outline-warning").click()

    # 4. Ожидать появления результата ровно 45 секунд
    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # 5. Проверить результат
    result_text = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert "15" in result_text, (
        f"Ожидался результат 15, получено: {result_text}")
    print("Тест пройден! Результат 15 отобразился корректно")
