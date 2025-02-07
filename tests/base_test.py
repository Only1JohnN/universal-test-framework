import pytest
import json
from selenium import webdriver
from utils.logger import setup_logger

logger = setup_logger(__name__, log_file='./logs/base_test.log')

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self, request):
        # Load configuration from config.json
        with open("config/config.json") as f:
            config = json.load(f)
        options = webdriver.ChromeOptions()
        # TODO: Uncomment for headless execution if desired
        # options.add_argument("--headless")
        logger.info("Setting up Chrome driver for test.")
        self.driver = webdriver.Chrome(executable_path=config["web"]["driver_path"], options=options)
        self.driver.get(config["web"]["base_url"])
        # Make the driver available to tests in classes that inherit BaseTest.
        request.cls.driver = self.driver
        yield
        logger.info("Quitting Chrome driver.")
        self.driver.quit()
