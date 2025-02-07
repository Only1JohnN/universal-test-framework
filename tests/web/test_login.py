import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BaseTest):

    @allure.feature("Login")
    @allure.story("Valid Login")
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        with allure.step("Enter username and password"):
            login_page.enter_username("testuser")        # TODO: Replace with dynamic credentials if needed
            login_page.enter_password("password123")       # TODO: Replace with dynamic credentials if needed
        with allure.step("Click login button"):
            login_page.click_login()
        with allure.step("Verify that dashboard is reached"):
            # Using an explicit wait instead of sleep for robustness
            WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
            assert "dashboard" in self.driver.current_url, "Dashboard not reached after login"
