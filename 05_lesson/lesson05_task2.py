from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def click_dynamic_id_button():
    """
    Упражнение 2: Клик по кнопке с динамическим ID.
    """

    # Настройка драйвера с автоматической установкой ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        print("✓ Страница загружена")

        # Ждем загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Находим кнопку по классу
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )

        # Получаем атрибуты кнопки для информации
        button_text = blue_button.text
        button_classes = blue_button.get_attribute("class")
        dynamic_id = blue_button.get_attribute("id")

        print(f"✓ Найдена кнопка: '{button_text}'")
        print(f"✓ Классы кнопки: {button_classes}")
        print(f"✓ Динамический ID: {dynamic_id}")

        # Проверяем, что кнопка отображается и кликабельна
        assert blue_button.is_displayed(), "Кнопка не отображается"
        assert blue_button.is_enabled(), "Кнопка не активна"

        # Кликаем по кнопке
        blue_button.click()
        print("✓ Клик по кнопке с динамическим ID выполнен")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎉 Задание выполнено успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:
        # Всегда закрываем браузер
        driver.quit()
        print("✓ Браузер закрыт")


def demonstrate_dynamic_id():
    """Дополнительная функция для демонстрации изменения ID."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("\n--- Демонстрация динамического ID ---")

        # Открываем страницу несколько раз чтобы показать изменение ID
        for i in range(3):
            driver.get("http://uitestingplayground.com/dynamicid")
            blue_button = driver.find_element(
                By.CSS_SELECTOR, "button.btn-primary"
            )
            dynamic_id = blue_button.get_attribute("id")
            print(f"Загрузка {i+1}: ID кнопки = {dynamic_id}")

            # Обновляем страницу для нового ID
            if i < 2:
                driver.refresh()

    finally:
        driver.quit()


if __name__ == "__main__":
    # Основной вызов
    click_dynamic_id_button()
