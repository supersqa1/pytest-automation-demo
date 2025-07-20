import pytest

@pytest.fixture
def setup_and_teardown():
    """
    A simple fixture to demonstrate setup and teardown.
    Code before 'yield' is the setup part.
    Code after 'yield' is the teardown part.
    """
    print("\n--- SETUP: This runs before the test ---")
    yield
    print("\n--- TEARDOWN: This runs after the test ---")



@pytest.mark.usefixtures("setup_and_teardown")
def test_example_using_usefixtures_decorator():
    """
    This test uses the fixture via the 'usefixtures' marker.
    This is used when the test does not need to access a return value from the fixture.
    """
    print("\n>>> I am the test and I am running now.")
    assert True 