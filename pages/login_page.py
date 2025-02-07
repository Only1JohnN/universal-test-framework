import logging
from selenium.webdriver.common.by import By
from utils.logger import setup_logger

# Set up a logger for this module.
logger = setup_logger(__name__, log_file='./logs/login_page.log')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # TODO: Update the locators as per your application's DOM.
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")
        logger.debug("LoginPage initialized with provided driver.")

    def enter_username(self, username):
        logger.info(f"Entering username: {username}")
        element = self.driver.find_element(*self.username_field)
        element.clear()  # Clear any pre-populated text
        element.send_keys(username)
    
    def enter_password(self, password):
        logger.info("Entering password.")
        element = self.driver.find_element(*self.password_field)
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        logger.info("Clicking login button.")
        self.driver.find_element(*self.login_button).click()
