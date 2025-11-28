from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

def input_field_operations():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        
        input_field = driver.find_element(By.TAG_NAME, "input")
        
        # Вводим "Sky", очищаем, вводим "Pro"
        input_field.send_keys("Sky")
        time.sleep(1)
        input_field.clear()
        time.sleep(1)
        input_field.send_keys("Pro")
        time.sleep(2)
        
        print("Упражнение 3 выполнено успешно!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    input_field_operations()
