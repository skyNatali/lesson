from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    # Находим поле ввода и вводим текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Находим кнопку и нажимаем
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ожидаем, пока текст кнопки не станет "SkyPro"
    wait = WebDriverWait(driver, 10)
    # Используем ожидание, что текст элемента станет равным "SkyPro"
    wait.until(EC.text_to_be_present_in_element
               ((By.ID, "updatingButton"), "SkyPro"))

    # Получаем текст кнопки
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)  # Должно вывести "SkyPro"

finally:
    driver.quit()
