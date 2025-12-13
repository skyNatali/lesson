from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

try:
    # Шаг 1: Дождаться загрузки всех картинок
    # Ожидаем, что текст "Please wait until the images are loaded..." исчезнет
    wait = WebDriverWait(driver, 10)
    loading_text_locator = (
        By.XPATH, "//p[contains(text(), 'Please wait')]"
    )
    wait.until(EC.invisibility_of_element_located(loading_text_locator))

    # Шаг 2: Найти все загруженные изображения
    images = driver.find_elements(By.TAG_NAME, "img")

    # Шаг 3: Получить значение атрибута 'src' у 3-й картинки (индекс 2)
    third_image_src = images[2].get_attribute("src")

    # Шаг 4: Вывести значение в консоль
    print(third_image_src)

finally:
    driver.quit()
