import json
import pytest
import time
import allure
from appium import webdriver
from utils.logger import setup_logger

logger = setup_logger(__name__, log_file='./logs/mobile_tests.log')

@pytest.fixture(scope="module")
def mobile_driver():
    with open("config/config.json") as f:
        config = json.load(f)
    desired_caps = config["mobile"]
    logger.info("Initializing mobile driver with desired capabilities.")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    logger.info("Quitting mobile driver.")
    driver.quit()

@allure.feature("Mobile Testing")
@allure.story("Checkout Flow")
def test_mobile_checkout(mobile_driver):
    with allure.step("Find and click the checkout button"):
        # TODO: Replace 'checkout' with your actual accessibility ID.
        checkout_button = mobile_driver.find_element_by_accessibility_id("checkout")
        checkout_button.click()
        logger.info("Clicked on checkout button.")
    with allure.step("Verify checkout header is displayed"):
        # TODO: Replace 'checkout_header' with the actual element ID in your mobile app.
        time.sleep(2)  # TODO: Replace with explicit wait for mobile elements if possible.
        header = mobile_driver.find_element_by_id("checkout_header")
        assert header.is_displayed(), "Checkout header is not displayed"
        logger.info("Checkout header displayed as expected.")
