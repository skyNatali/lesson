from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def input_field_operations():
    """Упражнение 3: Работа с полем ввода в Chrome."""

    # Настройка драйвера Chrome с автоматической установкой
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открываем страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        print("✓ Страница загружена")

        # Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # Проверяем, что поле найдено и доступно
        assert input_field.is_displayed(), "Поле ввода не отображается"
        assert input_field.is_enabled(), "Поле ввода не активно"

        print("✓ Поле ввода найдено")

        # Вводим текст "Sky"
        input_field.send_keys("Sky")
        print("✓ Введен текст: 'Sky'")

        # Проверяем, что текст введен
        current_value = input_field.get_attribute("value")
        print(f"✓ Текущее значение поля: '{current_value}'")

        # Небольшая пауза для наглядности
        time.sleep(2)

        # Очищаем поле
        input_field.clear()
        print("✓ Поле очищено")

        # Проверяем, что поле пустое
        current_value_after_clear = input_field.get_attribute("value")
        print(f"✓ Значение после очистки: '{current_value_after_clear}'")

        # Вводим текст "Pro"
        input_field.send_keys("Pro")
        print("✓ Введен текст: 'Pro'")

        # Проверяем финальное значение
        final_value = input_field.get_attribute("value")
        print(f"✓ Финальное значение поля: '{final_value}'")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎉 Все операции с полем ввода выполнены успешно!")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

    finally:
        # Закрываем браузер
        driver.quit()
        print("✓ Браузер закрыт")


def alternative_locators_version():
    """Альтернативная версия с разными способами поиска поля."""

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        print("✓ Страница загружена")

        # Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # Выполняем операции с полем
        input_field.send_keys("Sky")
        print("Введено: 'Sky'")

        time.sleep(1)
        input_field.clear()
        print("Поле очищено")

        time.sleep(1)
        input_field.send_keys("Pro")
        print("Введено: 'Pro'")

        time.sleep(2)
        print("🎉 Операции завершены!")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    # Основной вызов
    input_field_operations()
