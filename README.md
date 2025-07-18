# PyTest Automation Framework for Ecommerce Site (Demo)

A demonstration test automation framework using Python, Pytest, and Selenium WebDriver. This project serves as a learning resource for building robust test automation frameworks and implementing best practices.

## Overview

This framework demonstrates:
- Frontend testing using Selenium WebDriver
- Backend API testing
- Page Object Model (POM) design pattern
- Environment configuration management
- Advanced test reporting

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
