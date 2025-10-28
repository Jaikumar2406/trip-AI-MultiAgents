from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_hotels(city: str, check_in: str = "", check_out: str = "") -> str:
    """
    Search for hotels in a given city using DuckDuckGo.

    Args:
        city (str): The city where hotels are needed (e.g., "Delhi")
        check_in (str): Optional check-in date (e.g., "2025-05-24")
        check_out (str): Optional check-out date (e.g., "2025-05-26")

    Returns:
        str: Snippets or summaries of hotel listings and prices.
    """
    date_part = f" from {check_in} to {check_out}" if check_in and check_out else ""
    query = f"hotels in {city}{date_part} with prices"
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    return results