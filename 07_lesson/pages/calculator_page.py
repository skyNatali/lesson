from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        """Установить значение в поле задержки"""
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))
    
    def click_button(self, button_text):
        """Нажать кнопку с указанным текстом"""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()
    
    def get_result(self, timeout=46):
        """Получить результат с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, "15"))
        return self.driver.find_element(*self.result_screen).text
    
    def perform_calculation(self, delay, sequence):
        """
        Выполнить последовательность операций
        
        :param delay: задержка в секундах
        :param sequence: список кнопок для нажатия, например ['7', '+', '8', '=']
        """
        self.set_delay(delay)
        for button in sequence:
            self.click_button(button)
