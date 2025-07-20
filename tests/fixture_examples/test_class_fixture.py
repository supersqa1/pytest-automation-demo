import pytest

@pytest.fixture(scope="class")
def setup_class_data(request):
    """
    This fixture has 'class' scope and uses the 'request' object
    to attach data directly to the test class.
    """
    print("\n--- SETUP: (CLASS SCOPE) Setting up data for the test class ---")
    # Dynamically attach an attribute to the test class
    request.cls.user_id = 101
    request.cls.username = "class_user"
    yield
    print("\n--- TEARDOWN: (CLASS SCOPE) Tearing down class data ---")


@pytest.mark.usefixtures("setup_class_data")
class TestUserActions:
    """
    A test class that uses the class-scoped fixture.
    The fixture sets up data that is shared across all methods in this class.
    """
    def test_get_user_info(self):
        print(f"\n>>> Running test_get_user_info for user_id: {self.user_id}")
        assert self.user_id == 101

    def test_delete_user(self):
        print(f"\n>>> Running test_delete_user for username: {self.username}")
        assert self.username == "class_user" 