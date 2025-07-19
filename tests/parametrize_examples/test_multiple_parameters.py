import pytest

# A simple helper function for the test to use.
# In a real project, this would be in a separate utility file.
def is_strong_password(password):
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    is_long_enough = len(password) >= 8
    return has_uppercase and has_digit and is_long_enough


@pytest.mark.parametrize("password, expected_result", [
    ("short", False),
    ("nouppercase123", False),
    ("NoDigits", False),
    ("A_Good_P@ssw0rd", True)
], ids=["Too Short", "No Uppercase", "No Digits", "Valid Password"])
def test_password_strength(password, expected_result):
    """
    This is the ideal use case for parametrize: testing a single function
    with multiple data combinations and expected outcomes.
    The 'ids' make the test report very easy to read.
    """
    print(f"\nTesting password: '{password}'")
    assert is_strong_password(password) == expected_result 