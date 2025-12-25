import pytest
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
    """Фикстура для создания и закрытия драйвера Firefox"""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_checkout(browser):
    # 1. Авторизация
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    
    # 2. Добавление товаров в корзину
    main_page = MainPage(browser)
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Onesie"
    ]
    
    for product in products_to_add:
        main_page.add_product_to_cart(product)
        print(f"Добавлен товар: {product}")
    
    # 3. Переход в корзину
    main_page.go_to_cart()
    
    # 4. Оформление заказа
    cart_page = CartPage(browser)
    cart_page.checkout()
    
    # 5. Заполнение формы оформления заказа
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_info(FIRST_NAME, LAST_NAME, ZIP_CODE)
    
    # 6. Получение и проверка итоговой суммы
    actual_total = checkout_page.get_total_amount()
    print(f"Итоговая сумма: ${actual_total}")
    
    # 7. Проверка assert
    assert actual_total == EXPECTED_TOTAL, (
        f"Ожидаемая сумма: ${EXPECTED_TOTAL}, "
        f"Фактическая сумма: ${actual_total}"
    )
    
    # Опционально: завершение покупки
    checkout_page.finish_checkout()
