import pytest

@pytest.fixture
def user_credentials():
    """
    A fixture that provides test data (e.g., from a config or created on the fly).
    It yields a dictionary of credentials.
    """
    print("\n--- SETUP: Getting user credentials ---")
    credentials = {
        "username": "admas_supersqa",
        "password": "SecurePassword123!"
    }
    yield credentials
    print("\n--- TEARDOWN: Cleaning up credentials ---")


def test_login_with_user_credentials(user_credentials):
    """
    This test uses the fixture by passing it as an argument.
    This allows the test to access the value yielded by the fixture.
    """
    print("\n>>> I am the test and I am running now.")
    print(f"Logging in with user: '{user_credentials['username']}'")
    assert user_credentials["username"] == "admas_supersqa"
    assert len(user_credentials["password"]) > 10 