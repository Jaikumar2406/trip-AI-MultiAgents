from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def describe_location_beauty(city: str) -> str:
    """
    Search for a brief description of the beauty of a given location.
    
    Args:
        city (str): The city to describe (e.g., "Mumbai").
        
    Returns:
        str: A brief description of the city's beauty (2 lines).
    """
    query = f"how beautiful is {city} description"
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    
    return results