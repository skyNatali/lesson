from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера и переход на страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # 2. Найти и нажать на синюю кнопку
    ajax_button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    ajax_button.click()

    # 3. Ожидание появления зеленой плашки с текстом
    # Элемент появляется через ~15 секунд после нажатия кнопки
    wait = WebDriverWait(driver, 20)  # Ждем до 20 секунд
    success_label = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # 4. Получение и вывод текста из зеленой плашки
    loaded_text = success_label.text
    print(loaded_text)  # "Data loaded with AJAX get request."

finally:
    # 5. Закрытие браузера
    driver.quit()
