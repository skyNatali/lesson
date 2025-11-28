from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time


def login_and_get_message():
    """Упражнение 4: Авторизация на сайте и получение сообщения."""

    # Настройка драйвера Chrome
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Открываем страницу логина
        driver.get("http://the-internet.herokuapp.com/login")
        print("✓ Страница логина загружена")

        # Находим поле username и вводим значение
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("✓ Введен username: tomsmith")

        # Находим поле password и вводим значение
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("✓ Введен password: SuperSecretPassword!")

        # Находим и нажимаем кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR,
                                           "button[type='submit']")
        login_button.click()
        print("✓ Нажата кнопка Login")

        # Ждем появления зеленой плашки с сообщением
        wait = WebDriverWait(driver, 10)
        success_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Получаем текст из зеленой плашки
        message_text = success_message.text
        print("✓ Текст с зеленой плашки:")
        print("-" * 50)
        print(message_text.strip())
        print("-" * 50)

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎉 Авторизация выполнена успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:
        # Закрываем браузер
        driver.quit()
        print("✓ Браузер закрыт")


def login_with_alternative_locators():
    """Альтернативная версия с разными способами поиска элементов."""

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("http://the-internet.herokuapp.com/login")
        print("✓ Страница логина загружена")

        # Для username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")

        # Для password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        # Для кнопки Login
        login_button = driver.find_element(By.CSS_SELECTOR,
                                           "button[type='submit']")
        login_button.click()

        # Ждем успешной авторизации
        wait = WebDriverWait(driver, 10)
        success_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "success"))
        )

        # Выводим текст сообщения
        message_text = success_message.text
        print("✓ Сообщение об успешной авторизации:")
        print(message_text.split('\n')[0])

        time.sleep(2)

    finally:
        driver.quit()


if __name__ == "__main__":
    # Основной вызов
    login_and_get_message()
