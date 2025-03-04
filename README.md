# PyTest Automation Framework for Ecommerce Site (Demo)

A demonstration test automation framework using Python, Pytest, and Selenium WebDriver. This project serves as a learning resource for building test automation frameworks and implementing CI/CD pipelines.

## Overview

This framework demonstrates:
- Frontend testing using Selenium WebDriver
- Backend API testing
- Page Object Model design pattern
- Environment configuration management
- Test reporting

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

Basic test execution:
```
    # Run all tests
    pytest

    # Run specific test types
    pytest tests/frontend/  # UI tests only
    pytest tests/backend/   # API tests only

    # Generate HTML report
    pytest --html=report.html
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
