import pytest

# --- Example 1: Without custom test IDs ---

@pytest.mark.parametrize("search_term", [
    "pytest",
    "fixtures",
    "selenium"
])
def test_search_bar_without_ids(search_term):
    """
    Demonstrates parametrizing a single argument.
    The test output will use the parameter value as the default ID.
    """
    print(f"\nSearching for: {search_term}")
    assert len(search_term) > 0


# --- Example 2: With custom, readable test IDs ---

@pytest.mark.parametrize("search_term", [
    "pytest",
    "fixtures",
    "selenium"
], ids=["Search for 'pytest'", "Search for 'fixtures'", "Search for 'selenium'"])
def test_search_bar_with_ids(search_term):
    """
    Demonstrates the 'ids' argument to provide clear, readable names
    for each test run in the report.
    """
    print(f"\nSearching for: {search_term}")
    assert len(search_term) > 0 