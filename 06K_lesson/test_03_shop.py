import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


# Данные для авторизации и оформления заказа
USERNAME = "standard_user"
PASSWORD = "secret_sauce"  # стандартный пароль для этого пользователя
FIRST_NAME = "Natali"
LAST_NAME = "Loc"
ZIP_CODE = "302023"
EXPECTED_TOTAL = "$58.29"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.FirefoxOptions()
    # Инициализация драйвера
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options)
    yield driver
    driver.quit()


def test_saucedemo(browser):
    # 1. Переход на страницу
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизация
    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(USERNAME)
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()

    # 3. Добавление товаров в корзину
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for item in items:
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[data-test='{item}']")))
        button.click()
        print(f"Добавлен товар: {item.replace('add-to-cart-', '')}")

    # 4. Переход в корзину
    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # 5. Начало оформления заказа
    browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    # 6. Заполнение формы
    browser.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys(FIRST_NAME)
    browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(LAST_NAME)
    browser.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys(ZIP_CODE)
    browser.find_element(By.CSS_SELECTOR, "#continue").click()

    # 7. Проверка итоговой суммы
    total_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_element.text
    total_value = total_text.split()[-1]

    assert total_value == EXPECTED_TOTAL, (
        f"Ожидалась сумма {EXPECTED_TOTAL}, получено {total_value}")
    print(f"Тест пройден! Итоговая сумма: {total_value}")
