import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="module")
def browser():
    # Настройка драйвера Edge
    driver = webdriver.Edge(service=Service(
        executable_path='C:/Users/Сергей/Desktop/Edge/msedgedriver.exe'))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(browser):
    # Открытие страницы
    browser.get
    ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")

    browser.find_element(
        By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # Нажатие кнопки Submit
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка подсветки полей
    # 1. Проверяем, что Zip code подсвечен красным
    zip_code_alert = browser.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_alert.get_attribute(
        "class"), "Поле Zip code не подсвечено красным"

    # 2. Проверяем, что остальные поля подсвечены зеленым
    success_fields = [
        ("#first-name", "Иван"),
        ("#last-name", "Петров"),
        ("#address", "Ленина, 55-3"),
        ("#e-mail", "test@skypro.com"),
        ("#phone", "+7985899998787"),
        ("#city", "Москва"),
        ("#country", "Россия"),
        ("#job-position", "QA"),
        ("#company", "SkyPro")
    ]

    for field_id, expected_value in success_fields:
        element = browser.find_element(By.CSS_SELECTOR, field_id)
        assert "alert-success" in element.get_attribute(
            "class"), f"Поле {field_id} не подсвечено зеленым"
        assert expected_value in element.text, (
            f"Значение в поле {field_id} не соответствует ожидаемому")
