import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Константы с тестовыми данными
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Natalia"
LAST_NAME = "Lokteva"
ZIP_CODE = "123456"
EXPECTED_TOTAL = "58.29"


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия драйвера Firefox."""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Оформление заказа в интернет-магазине")
@allure.description("Полный тест процесса покупки: авторизация, добавление товаров, оформление заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout(browser):
    """
    Полный тест процесса покупки в интернет-магазине.
    
    Шаги:
    1. Авторизация в системе
    2. Добавление товаров в корзину
    3. Переход в корзину
    4. Оформление заказа
    5. Проверка итоговой суммы
    """
    with allure.step("Авторизация в системе"):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)
        allure.attach(browser.get_screenshot_as_png(), 
                     name="После авторизации",
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(browser)
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for product in products_to_add:
            with allure.step(f"Добавить товар: {product}"):
                main_page.add_product_to_cart(product)
    
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
        allure.attach(browser.get_screenshot_as_png(),
                     name="Корзина с товарами",
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Оформление заказа"):
        cart_page = CartPage(browser)
        cart_page.checkout()
    
    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_checkout_info(FIRST_NAME, LAST_NAME, ZIP_CODE)
    
    with allure.step("Получение итоговой суммы"):
        actual_total = checkout_page.get_total_amount()
        allure.attach(browser.get_screenshot_as_png(),
                     name="Итоговая сумма",
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step(f"Проверка итоговой суммы (ожидаемо: ${EXPECTED_TOTAL}, фактически: ${actual_total})"):
        assert actual_total == EXPECTED_TOTAL, (
            f"Ожидаемая сумма: ${EXPECTED_TOTAL}, "
            f"Фактическая сумма: ${actual_total}"
        )
    
    with allure.step("Завершение покупки"):
        checkout_page.finish_checkout()
