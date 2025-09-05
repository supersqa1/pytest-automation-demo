import pytest

# --- Example 2: With custom, readable test IDs ---

@pytest.mark.parametrize("search_term", ["t-shirt", "pdf","purified water"], 
                         ids=["Search for 't-shirt'", "Search for 'pdf'", "Search for 'purified water'"])
def test_search_bar_with_ids(search_term):
    """
    Demonstrates the 'ids' argument to provide clear, readable names
    for each test run in the report.
    """
    print(f"\nSearching for: {search_term}")
    assert len(search_term) > 0 