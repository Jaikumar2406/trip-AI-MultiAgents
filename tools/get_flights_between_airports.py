from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def get_flights_between_airports(from_city: str, to_city: str) -> str:
    """
    Search for available flights and prices from one city to another using DuckDuckGo.
    
    Args:
        from_city (str): Departure city (e.g., "Mumbai")
        to_city (str): Destination city (e.g., "Delhi")

    Returns:
        str: Search result snippets or summaries.
    """
    query = f"flights from {from_city} to {to_city} with prices today"
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    return results