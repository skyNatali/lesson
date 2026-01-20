from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора."""
    
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        
        :param driver: WebDriver instance для управления браузером
        :type driver: selenium.webdriver.Chrome or selenium.webdriver.Firefox
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
    
    def open(self) -> None:
        """
        Открыть страницу калькулятора.
        
        :return: None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds: int) -> None:
        """
        Установить значение в поле задержки.
        
        :param seconds: Количество секунд задержки
        :type seconds: int
        :return: None
        """
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(seconds))
    
    def click_button(self, button_text: str) -> None:
        """
        Нажать кнопку с указанным текстом.
        
        :param button_text: Текст на кнопке (например, "7", "+", "=")
        :type button_text: str
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()
    
    def get_result(self, timeout: int = 45) -> str:
        """
        Получить результат с ожиданием.
        
        :param timeout: Максимальное время ожидания в секундах
        :type timeout: int
        :return: Текстовое значение результата
        :rtype: str
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, "15"))
        return self.driver.find_element(*self.result_screen).text
    
    def perform_calculation(self, delay: int, sequence: list) -> None:
        """
        Выполнить последовательность операций.
        
        :param delay: Задержка в секундах
        :type delay: int
        :param sequence: Список кнопок для нажатия (например, ['7', '+', '8', '='])
        :type sequence: list
        :return: None
        """
        self.set_delay(delay)
        for button in sequence:
            self.click_button(button)
