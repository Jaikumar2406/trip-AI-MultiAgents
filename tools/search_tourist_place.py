from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_tourist_places(city: str) -> str:
    """
    Search for the top tourist places in a given city using DuckDuckGo.
    
    Args:
        city (str): The city to find tourist places in (e.g., "Mumbai").
        
    Returns:
        str: Search result snippets or summaries of tourist places.
    """
    query = f"tourist places in {city}"
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    return results