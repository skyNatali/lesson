from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины покупок."""
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        
        :param driver: WebDriver instance для управления браузером
        :type driver: selenium.webdriver.Chrome or selenium.webdriver.Firefox
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
    
    def checkout(self) -> None:
        """
        Нажать кнопку оформления заказа.
        
        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()
