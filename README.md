# PyTest Automation Framework for Ecommerce Site (Demo)

A demonstration test automation framework using Python, Pytest, and Selenium WebDriver. This project serves as a learning resource for building robust test automation frameworks and implementing best practices.

## Overview

This framework demonstrates:
- Frontend testing using Selenium WebDriver
- Backend API testing
- Page Object Model (POM) design pattern
- Environment configuration management
- Advanced test reporting

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Markers for Organization and Selection](#markers-for-organization-and-selection)
- [Mastering Fixtures for Setup and Teardown](#mastering-fixtures-for-setup-and-teardown)
- [Data-Driven Testing with @parametrize](#data-driven-testing-with-parametrize)
- [Speeding Up Test Runs with Parallel Execution](#speeding-up-test-runs-with-parallel-execution)
- [Generating Rich Test Reports with Allure](#generating-rich-test-reports-with-allure)
- [Test Categories](#test-categories)
- [Configuration](#configuration)
- [Test Reports](#test-reports)
- [Best Practices](#best-practices)
- [Support](#support)

## Project Structure
```
    pytest-automation-demo/
    ├── config/
    │   └── config.py           # Environment configuration
    ├── pages/
    │   ├── base_page.py       # Base page object
    │   ├── home_page.py       # Home page object
    │   └── my_account_page.py # Account page object
    ├── tests/
    │   ├── frontend/          # UI tests
    │   │   ├── test_home_page.py
    │   │   └── test_my_account.py
    │   └── backend/           # API tests
    │       ├── test_create_customer.py
    │       └── test_orders_api.py
    ├── .env                   # Environment variables
    ├── conftest.py           # Pytest fixtures
    ├── requirements.txt
    └── README.md
```

## Setup

### Prerequisites
- Python 3.11+
- Chrome or Firefox browser

### Installation
1. Clone the repository
2. Create virtual environment:

    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:
```
    pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and update configuration

## Running Tests

This section covers how PyTest discovers and executes tests, including command-line options and best practices.

### Basic Test Execution

The simplest way to run all tests in your project:

```bash
pytest tests
```

This command automatically discovers and runs all test files in your project. PyTest will search for files that match the naming pattern `test_*.py` or `*_test.py` and execute all functions that start with `test_`.

### Test Discovery

PyTest follows these rules to automatically discover tests:

**File Naming Rules:**
- Files must start with `test_` OR end with `_test.py`
- Examples: `test_home_page.py`, `login_test.py`, `user_test.py`

**Function Naming Rules:**
- Functions must start with `test_`
- Examples: `test_user_login()`, `test_checkout_flow()`, `test_api_response()`

**Class Naming Rules:**
- Classes must start with `Test` (capital T)
- Classes should NOT have an `__init__` method
- **Note:** Classes are optional - you can write tests as standalone functions
- Examples: `TestHomePage`, `TestUserAccount`, `TestAPIEndpoints`

PyTest searches recursively through directories starting from where you run the command.

### Targeted Test Execution

While `pytest` runs everything, you can be more specific about which tests to execute:

**Run tests in a specific directory:**
```bash
pytest tests/frontend/
pytest tests/backend/
```

**Run tests by keyword (partial match):**
```bash
pytest -k "login"
pytest -k "account"
pytest -k "customer"
```

**Exclude tests using NOT:**
```bash
pytest -k "not slow"
pytest -k "not integration"
pytest -k "not TestHomePage"
```

**Explanation:** The `not` keyword excludes tests that match the pattern. `pytest -k "not TestHomePage"` will run all tests EXCEPT those in the `TestHomePage` class.

**Combine conditions using AND/OR:**
```bash
pytest -k "login or register"
pytest -k "home and not slow"
pytest -k "(login or logout) and not api"
```

**Explanation:** 
- `or` runs tests that match either condition
- `and` requires tests to match both conditions
- `pytest -k "login or register"` runs tests with "login" OR "register" in the name
- `pytest -k "home and not slow"` runs tests with "home" in the name BUT excludes those with "slow"
- Parentheses group conditions: `(login or logout) and not api` runs login/logout tests but excludes API tests

**Note:** The `-k` flag matches against test names (function names, class names, and file names), not just function names.

**Run specific test files:**
```bash
pytest tests/frontend/test_home_page.py
pytest tests/backend/test_orders_api.py
```

**Run specific test functions:**
```bash
pytest tests/frontend/test_home_page.py::test_home_page_loads
pytest tests/backend/test_orders_api.py::test_create_order
```

**Run specific test classes:**
```bash
pytest tests/frontend/test_home_page.py::TestHomePage
pytest tests/backend/test_orders_api.py::TestOrdersAPI
```

**Run specific methods within classes:**
```bash
pytest tests/frontend/test_home_page.py::TestHomePage::test_navigation
pytest tests/backend/test_orders_api.py::TestOrdersAPI::test_order_creation
```

### Useful Command-Line Flags

**Verbose output (shows each test function):**
```bash
pytest -v
```

**Show print statements and output (captures stdout/stderr):**
```bash
pytest -s
```

**Note:** The `-s` flag shows print statements, logging output, and any other stdout/stderr that would normally be captured by PyTest.

**Combine verbose and show output:**
```bash
pytest -v -s
```

**Dry run - collect tests without running them:**
```bash
pytest --collect-only
```

**Generate HTML report:**
```bash
pytest --html=report.html
```

**Stop on first failure:**
```bash
pytest -x
```

**Run tests in parallel (requires pytest-xdist):**
```bash
pytest -n auto
```

### Common Discovery Issues

**Tests not being discovered:**
- Check file naming: must start with `test_` or end with `_test.py`
- Check function naming: must start with `test_`
- Check class naming: must start with `Test` (capital T)
- Ensure files are in the correct directory structure

**Import errors during discovery:**
```bash
# Check what tests PyTest can see
pytest --collect-only

# Debug import issues
pytest --tb=short
```

**Explanation:** `--tb=short` shows a shorter, more focused traceback that helps identify import and discovery problems without overwhelming output.

**Tests running from wrong location:**
```bash
# Run from project root to ensure proper discovery
cd /path/to/your/project
pytest

# Or specify the test directory explicitly
pytest tests/
```

**Slow discovery in large projects:**
```bash
# Clear cache if discovery is slow
pytest --cache-clear

# Run only specific directories to speed up discovery
pytest tests/frontend/ --cache-clear
```

## Markers for Organization and Selection

PyTest markers allow you to categorize, organize, and selectively run tests based on their characteristics or metadata.

### Built-in Markers

**Skip tests unconditionally:**
```python
@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    pass
```

**Skip tests conditionally:**
```python
import sys

@pytest.mark.skipif(sys.version_info > (3, 7), reason="Requires Python 3.8+")
def test_python_version_dependent():
    pass
```

**Mark tests as expected to fail:**
```python
@pytest.mark.xfail(reason="Known bug in API")
def test_broken_api():
    # This test is expected to fail
    response = api_call()
    assert response.status_code == 200
```

### Custom Markers

**Create your own markers for test categorization:**
```python
@pytest.mark.smoke
def test_login_functionality():
    pass

@pytest.mark.regression
def test_complex_workflow():
    pass

@pytest.mark.slow
def test_performance_heavy():
    pass
```

**Run tests by marker:**
```bash
pytest -m smoke
pytest -m "not slow"
pytest -m "smoke or regression"
```

**Note:** If you see `PytestUnknownMarkWarning`, you need to register your markers in `pytest.ini`:
```ini
[pytest]
markers =
    smoke: marks tests as smoke tests
    regression: marks tests as regression tests
    slow: marks tests as slow running
```

### Markers with Arguments (for Metadata)

**Add metadata to tests using marker arguments:**
```python
@pytest.mark.tcid('TCID-123')
def test_user_registration():
    pass

@pytest.mark.tcid('TCID-456')
def test_user_login():
    pass

@pytest.mark.priority('high')
def test_critical_feature():
    pass
```

**Register markers with arguments in `pytest.ini`:**
```ini
[pytest]
markers =
    tcid: test case identifier
    priority: test priority level
```

### Running Tests by Marker Argument

**Run tests based on marker argument values:**
```bash
pytest --tcid TCID-123
pytest --tcid TCID-456
```

**Note:** The `--tcid` flag implementation is available in the `conftest.py` file. This allows you to run specific tests by their Test Case ID.

## Mastering Fixtures for Setup and Teardown

Fixtures are a powerful PyTest feature used to provide a fixed baseline for tests. They are primarily used for setup and teardown code to reduce duplication, following the **DRY (Don't Repeat Yourself)** principle. Fixtures help you create reusable test components that can be shared across multiple tests.

### The Anatomy of a Fixture (`yield`)

Modern fixtures use `yield` to separate setup from teardown. Code before `yield` is the setup part, and code after `yield` is the teardown part.

**Example:** See `tests/fixture_examples/test_basic_fixture_yield.py` for a complete demonstration.

```python
@pytest.fixture
def setup_and_teardown():
    print("--- SETUP: This runs before the test ---")
    yield  # Test runs here
    print("--- TEARDOWN: This runs after the test ---")
```

### Two Ways to Use a Fixture

#### 1. For Actions Only (`@pytest.mark.usefixtures`)

Use this when the test only needs the fixture's setup/teardown actions and does not need a return value.

```python
@pytest.mark.usefixtures("setup_and_teardown")
def test_example():
    # Test code here
    assert True
```

#### 2. To Provide Data (Passing as an Argument)

Use this when the test needs to access the object or data returned by the fixture.

**Example:** See `tests/fixture_examples/test_return_value_fixture.py` for a complete demonstration.

```python
@pytest.fixture
def user_credentials():
    credentials = {"username": "test_user", "password": "test_pass"}
    yield credentials
    # Cleanup code here

def test_login(user_credentials):
    # Access the returned data
    assert user_credentials["username"] == "test_user"
```

### Returning Multiple Items

For returning multiple values, using a **dictionary** is a recommended best practice for readability, as shown in the `test_return_value_fixture.py` example.

```python
@pytest.fixture
def test_data():
    data = {
        "user": "test_user",
        "email": "test@example.com",
        "role": "admin"
    }
    yield data
```

### Fixture Scope (The Key to Efficiency)

The `scope` parameter controls how often a fixture is created and destroyed. Using the right scope is crucial for performance.

**Common Scopes:**

- **`scope='function'`** (default): Runs once per test function
- **`scope='class'`**: Runs once per test class
- **`scope='session'`**: Runs once for the entire test session

**Example:** See `tests/fixture_examples/test_scope_fixture.py` for a complete demonstration.

```python
@pytest.fixture(scope="session")
def browser():
    # Expensive setup - only done once
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def test_data():
    # Lightweight setup - done for each test
    data = {"id": random.randint(1, 1000)}
    yield data
```

**Performance Tip:** Use `session` scope for expensive resources like browsers, databases, or API connections.

### The Magic of `conftest.py`

`conftest.py` is a special file where shared fixtures are placed. Any fixture defined in `conftest.py` is automatically available to all tests in that directory and its subdirectories, with no imports needed.

**Benefits:**
- **No imports required** - fixtures are automatically discovered
- **Shared across directories** - place in parent directory to share with subdirectories
- **Clean organization** - keeps fixtures separate from test logic

**Example structure:**
```
tests/
├── conftest.py          # Shared fixtures for all tests
├── frontend/
│   ├── conftest.py      # Frontend-specific fixtures
│   └── test_home.py
└── backend/
    ├── conftest.py      # Backend-specific fixtures
    └── test_api.py
```

## Data-Driven Testing with @parametrize

PyTest allows you to run a single test function with multiple sets of data using the `@pytest.mark.parametrize` decorator. This is a powerful feature for reducing code duplication and thoroughly testing your logic.

For detailed, commented examples covering basic usage, readable test IDs, and combining with other markers, please see the files inside the `tests/parametrize_examples/` directory.

## Speeding Up Test Runs with Parallel Execution

As a test suite grows, execution time can become a major bottleneck. The `pytest-xdist` plugin allows you to run your tests in parallel across multiple CPU cores to dramatically reduce this time.

**Installation:**
```bash
pip install pytest-xdist
```

**Basic Usage:**
The most common way to use it is with the `-n` flag, which specifies the number of parallel worker processes.

```bash
# Automatically use one worker per available CPU core
pytest -n auto

# Specify exact number of workers
pytest -n 4

# Use a conservative number of workers (useful for resource-intensive tests)
pytest -n 2
```

**Important Considerations:**

- **Test Independence:** Parallel execution only works correctly if your tests are completely independent and do not rely on the state or outcome of other tests.

- **Fixture Scope:** A session-scoped fixture (`@pytest.fixture(scope="session")`) will be created once per worker process, not once for the entire test run. This is a critical concept to understand when sharing resources.

## Generating Rich Test Reports with Allure

Allure is a powerful reporting framework that creates detailed, interactive test reports. It provides better visibility into test execution with features like step-by-step logs, test descriptions, and organized test hierarchies.

### Installation

**Install the Python package:**
```bash
pip install allure-pytest
```

**Install the Allure command-line tool:**
```bash
# macOS (using Homebrew)
brew install allure

# Windows (using Scoop)
scoop install allure

# Linux
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Basic Usage

**Run tests and generate Allure results:**
```bash
pytest --alluredir=./allure-results
```

**Generate and view the HTML report:**
```bash
# Generate HTML report
allure generate allure-results --clean

# Open the report in browser
allure open allure-report

# Or serve the report directly
allure serve allure-results
```

### Allure Decorators

**Test-level decorators for better reporting:**

```python
import allure

@allure.title("Test User Can Log In Successfully")
@allure.description("This test verifies that a registered user can log in with valid credentials.")
@allure.feature("Authentication")
@allure.story("User Login")
def test_login_with_valid_credentials():
    # Test code here
    pass
```

**Step-level decorators for detailed execution logs:**

```python
@allure.step("Entering username: {1}")
def enter_username(self, username):
    self.find_element(self.USERNAME_INPUT).send_keys(username)

@allure.step("Clicking the login button")
def click_login(self):
    self.find_element(self.LOGIN_BUTTON).click()
```

### Report Features

- **Test Hierarchy**: Organize tests by Features and Stories
- **Step-by-Step Execution**: See exactly what happened during test execution
- **Attachments**: Add screenshots, logs, or other files to test reports
- **Environment Information**: Track test environment details
- **Trends**: Compare test results over time

### Advanced Usage

**Add attachments to tests:**
```python
import allure

def test_with_attachment():
    # Test code here
    
    # Add screenshot or file to report
    allure.attach.file('screenshot.png', 'Screenshot', allure.attachment_type.PNG)
```

**Add environment information:**
```bash
# Create environment.properties file
echo "Browser=Chrome" > allure-results/environment.properties
echo "Version=4.34.0" >> allure-results/environment.properties
```

## Test Categories

### Frontend Tests
- Home page functionality
- Account management
- Login/Registration flows

### Backend Tests
- Customer API operations
- Order management API
- Basic CRUD operations

## Configuration

The framework uses a hierarchical configuration:
1. Environment variables
2. `.env` file
3. Default values in `config.py`

Example `.env` configuration:
```
    # Browser Configuration
    BROWSER=chrome
    HEADLESS=False
    IMPLICIT_WAIT=10

    # API Configuration
    API_URL=http://demostore.example.com
    API_KEY=your_key
    API_SECRET=your_secret
```

## Test Reports

Run tests with the HTML reporter:
```
    pytest --html=report.html
```

The report includes:
- Test execution summary
- Pass/Fail statistics
- Error logs
- Screenshots for failed UI tests

## Best Practices

- Use virtual environment
- Keep credentials in `.env`
- Run headless mode in CI/CD
- Write independent tests
- Follow Page Object pattern
- Add proper logging

## Support

For questions and support:
- Create an issue in the repository
- Check existing documentation
- Review closed issues

---

*This framework is designed for educational purposes and demonstrates test automation best practices.*
