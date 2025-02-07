import json
import requests
import pytest
import allure
from utils.logger import setup_logger

logger = setup_logger(__name__, log_file='./logs/api_tests.log')

@pytest.fixture(scope="module")
def api_config():
    with open("config/config.json") as f:
        config = json.load(f)
    logger.debug("Loaded API configuration.")
    return config["api"]

# Example of data-driven tests using parameterization.
@allure.feature("API Testing")
@allure.story("Get Users Endpoint")
@pytest.mark.parametrize("user_endpoint,expected_status", [
    ("/users", 200),
    # TODO: Add more endpoints and expected status codes as needed.
])
def test_get_users(api_config, user_endpoint, expected_status):
    url = f"{api_config['base_url']}{user_endpoint}"  # Ensure the endpoint is correct.
    with allure.step(f"Sending GET request to {url}"):
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url)
    with allure.step("Verify response status code"):
        logger.debug(f"Response status code: {response.status_code}")
        assert response.status_code == expected_status, f"Expected status code {expected_status}"
    with allure.step("Verify response data structure"):
        data = response.json()
        logger.debug("Received data from API.")
        assert isinstance(data, list), "Expected data to be a list"
