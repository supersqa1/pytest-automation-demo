import pytest

@pytest.fixture(scope="session")
def session_scoped_fixture():
    """
    This fixture has 'session' scope.
    It will run only ONCE for the entire test session.
    """
    print("\n--- SETUP: (SESSION SCOPE) This runs only once at the start ---")
    yield
    print("\n--- TEARDOWN: (SESSION SCOPE) This runs only once at the end ---")


@pytest.fixture(scope="function")
def function_scoped_fixture():
    """
    This fixture has 'function' scope (the default).
    It will run ONCE FOR EVERY TEST that uses it.
    """
    print("\n- SETUP: (FUNCTION SCOPE) Before each test -")
    yield
    print("\n- TEARDOWN: (FUNCTION SCOPE) After each test -")


def test_one_using_scopes(session_scoped_fixture, function_scoped_fixture):
    print("\n>>> Running Test One")
    assert True


def test_two_using_scopes(session_scoped_fixture, function_scoped_fixture):
    print("\n>>> Running Test Two")
    assert True 