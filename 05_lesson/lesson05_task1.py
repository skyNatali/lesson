from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def click_blue_button():
    """Функция для клика по синей кнопке на странице."""

    # Настройка драйвера с автоматической установкой ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/classattr")
        print("✓ Страница загружена")

        # Находим синюю кнопку по CSS-классу
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

        # Проверяем, что кнопка найдена и отображается
        assert blue_button.is_displayed(), "Синяя кнопка не отображается"
        print("✓ Синяя кнопка найдена")

        # Кликаем по кнопке
        blue_button.click()
        print("✓ Клик по синей кнопке выполнен")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎉 Задание выполнено успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:
        # Всегда закрываем браузер
        driver.quit()
        print("✓ Браузер закрыт")


if __name__ == "__main__":
    click_blue_button()
