from selenium.webdriver.common.by import By


class MainPage:
    """Page Object для главной страницы магазина."""
    
    def __init__(self, driver):
        """
        Инициализация главной страницы.
        
        :param driver: WebDriver instance для управления браузером
        :type driver: selenium.webdriver.Chrome or selenium.webdriver.Firefox
        """
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
    
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавить товар в корзину по его названию.
        
        :param product_name: Название товара
        :type product_name: str
        :return: None
        """
        product_id = self._get_product_id(product_name)
        add_button_locator = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*add_button_locator).click()
    
    def go_to_cart(self) -> None:
        """
        Перейти в корзину покупок.
        
        :return: None
        """
        self.driver.find_element(*self.shopping_cart).click()
    
    def _get_product_id(self, product_name: str) -> str:
        """
        Конвертировать название товара в ID продукта.
        
        :param product_name: Название товара
        :type product_name: str
        :return: ID продукта для использования в локаторах
        :rtype: str
        """
        product_ids = {
            "Sauce Labs Backpack": "sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "sauce-labs-onesie",
            "Sauce Labs Bike Light": "sauce-labs-bike-light",
            "Sauce Labs Fleece Jacket": "sauce-labs-fleece-jacket",
            "Test.allTheThings() T-Shirt (Red)": "test.allthethings()-t-shirt-(red)"
        }
        return product_ids.get(product_name, product_name.lower().replace(" ", "-"))
