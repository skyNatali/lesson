from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа."""
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        
        :param driver: WebDriver instance для управления браузером
        :type driver: selenium.webdriver.Chrome or selenium.webdriver.Firefox
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
    
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить информацию для оформления заказа.
        
        :param first_name: Имя покупателя
        :type first_name: str
        :param last_name: Фамилия покупателя
        :type last_name: str
        :param postal_code: Почтовый индекс
        :type postal_code: str
        :return: None
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму со страницы.
        
        :return: Итоговая сумма в виде строки (без символа $)
        :rtype: str
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        total_text = total_element.text
        return total_text.replace("Total: $", "")
    
    def finish_checkout(self) -> None:
        """
        Завершить оформление заказа.
        
        :return: None
        """
        self.driver.find_element(*self.finish_button).click()
