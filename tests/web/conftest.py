import pytest
import os
import sys
from pathlib import Path
import allure

# Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils.screenshot import take_screenshot

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # Only capture screenshot if the test phase is "call" and the test failed.
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            if screenshot_path and os.path.exists(screenshot_path):
                allure.attach.file(screenshot_path,
                                   name="Failure Screenshot",
                                   attachment_type=allure.attachment_type.PNG)
