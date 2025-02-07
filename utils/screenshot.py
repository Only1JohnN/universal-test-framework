import os
from datetime import datetime

def take_screenshot(driver, test_name):
    """
    Captures a screenshot and saves it to the './logs/screenshots' folder.
    Returns the screenshot file path.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "./logs/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    try:
        driver.save_screenshot(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None
