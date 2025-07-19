import pytest

# A simple helper function.
def is_valid_email_format(email):
    return "@" in email and "." in email.split("@")[1]


@pytest.mark.parametrize("email, expected_result", [
    # Wrap each tuple in pytest.param() to add marks or an id
    pytest.param("test@example.com", True, marks=@pytest.mark.tcid('TCID-501'), id="Valid Email"),
    pytest.param("invalid-email.com", False, marks=@pytest.mark.tcid('TCID-502'), id="Invalid No @"),
    pytest.param("another.test@domain.co.uk", True, marks=@pytest.mark.tcid('TCID-503'), id="Valid Subdomain"),
    pytest.param("user@", False, marks=@pytest.mark.tcid('TCID-504'), id="Invalid No Domain")
])
def test_email_validator_with_individual_tcids(email, expected_result):
    """
    This demonstrates assigning a unique marker to each parameter set.
    Now, each data row is linked to its own specific Test Case ID.
    """
    assert is_valid_email_format(email) == expected_result