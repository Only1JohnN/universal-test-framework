# Universal Test Automation Framework

This repository contains an **advanced** test automation framework for web, mobile, API, and performance testing. The framework now includes:

- **BaseTest Class:** Centralized WebDriver setup and teardown.
- **Global Pytest Hooks:** Automatically capture screenshots on test failure and attach them to Allure reports.
- **Allure Integration:** Enhanced reporting with step logging and attachments.
- **Data-Driven API Testing:** Example of parameterized tests.
- **Extensive Logging:** Centralized logging across modules with inline comments and TODOs for easy customization.

## Repository Structure

```
.
├── config
│   └── config.json
├── pages
│   └── login_page.py
├── tests
│   ├── api
│   │   └── test_users.py
│   ├── mobile
│   │   └── test_checkout.py
│   ├── web
│   │   ├── test_login.py
│   │   └── conftest.py
│   └── base_test.py
├── utils
│   ├── db_utils.py
│   ├── logger.py
│   └── screenshot.py
├── .github
│   └── workflows
│       └── ci.yml
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/universal-test-framework.git
   cd universal-test-framework
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environments:**
   - Update `config/config.json` with your target URLs, credentials, and driver paths.
   - Check inline comments in the code for other values to replace (e.g., element locators in `login_page.py`).

4. **Start Required Services:**
   - **Web Testing:** Ensure the ChromeDriver exists at the specified path.
   - **Mobile Testing:** Start an Appium server on `http://localhost:4723/wd/hub`.
   - **Performance Testing:** Integrate your JMeter scripts as needed.

5. **Run the Tests:**
   - All tests (web, API, and mobile):
     ```bash
     pytest
     ```

6. **Generating Allure Reports:**
   - Run your tests with Allure integration and generate a report:
     ```bash
     pytest --alluredir=./allure-results
     allure serve ./allure-results
     ```

## CI/CD

The GitHub Actions workflow in `.github/workflows/ci.yml` automatically installs dependencies and runs tests on push or pull request events.

## Extending the Framework

- **Logging:** Modify the logging configuration in `utils/logger.py` if you need different logging levels or handlers.
- **Element Locators:** Update locators in your Page Objects (e.g., `pages/login_page.py`) as needed.
- **Additional Tests:** Expand the test suite by adding new tests or modules.
- **Data-Driven Testing:** Leverage parameterization in Pytest for testing multiple scenarios.

---

This extended framework should serve as a robust foundation for showcasing your advanced QA engineering skills. Feel free to modify and extend further to meet your project's needs.

Happy testing!
```

This complete extended codebase incorporates advanced features and demonstrates best practices in test automation. You can further modify and expand it to showcase additional skills and integrate with your development workflow.

