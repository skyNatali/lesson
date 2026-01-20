from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации."""
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        
        :param driver: WebDriver instance для управления браузером
        :type driver: selenium.webdriver.Chrome or selenium.webdriver.Firefox
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def open(self) -> None:
        """
        Открыть страницу авторизации.
        
        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию.
        
        :param username: Имя пользователя
        :type username: str
        :param password: Пароль пользователя
        :type password: str
        :return: None
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
