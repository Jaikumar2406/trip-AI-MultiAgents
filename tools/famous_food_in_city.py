from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def famous_food_in_city(city: str) -> str:
    """
    Search for the famous food items in a given city using DuckDuckGo.

    Args:
        city (str): The city where food is being searched (e.g., "Mumbai")

    Returns:
        str: Search result snippets or summaries about famous dishes.
    """
    query = f"famous food in {city}"
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    return results