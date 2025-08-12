import asyncio
from lxml import html
import requests



async def mcp_catalog_lookup(query: str = ""):
    """
    Looks up the MCP catalog for a given query.
    """
    # Get the HTML content of the page
    response = await asyncio.to_thread(requests.get, "https://docs.docker.com/ai/mcp-catalog-and-toolkit/")
    response.raise_for_status()
    
    # Parse the HTML
    tree = html.fromstring(response.content)
    
    # Extract the tools
    tools = tree.xpath('//div[contains(@class, "prose")]//div[contains(@class, "card")]')
    
    results = []
    for tool in tools:
        tool_name_elements = tool.xpath('.//h3/text()')
        tool_description_elements = tool.xpath('.//p/text()')
        
        if tool_name_elements and tool_description_elements:
            tool_name = tool_name_elements[0].strip()
            tool_description = tool_description_elements[0].strip()
            
            if not query or query.lower() in tool_name.lower() or query.lower() in tool_description.lower():
                results.append(f"**{tool_name}**: {tool_description}")
            
    return results

async def mcp_toolkit_selector(query: str = ""):
    """
    Determines the best tool to use in the MCP toolkit after reviewing the catalog.
    """
    print(f"Finding the best tool for: {query}")
    
    results = await mcp_catalog_lookup(query)
    
    if results:
        print("Found the following tools:")
        print("\n".join(results))
        print("\nI recommend using the first tool from the list.")
        recommended_tool = results[0]
        print(recommended_tool)
        print("\nWould you like to build with this tool? (y/n)")

    else:
        print("No tools found for your query.")

async def ask_gordon(query: str = ""):
    """
    Simulates asking Gordon a question and provides a canned response.
    """
    print(f"Asking Gordon: {query}")
    if "docker" in query.lower():
        print("Gordon says: Docker is a platform designed to help developers build, share, and run applications using containers. Containers are a standardized unit of software that allows developers to package up an application and its dependencies into a single unit.")
    elif "mcp" in query.lower():
        print("Gordon says: MCP stands for Model Context Protocol. It's a standard that enables AI agents to interact with external systems and tools.")
    else:
        print("Gordon says: I'm sorry, I can only answer questions about Docker and MCP at the moment.")


if __name__ == '__main__':
    asyncio.run(mcp_toolkit_selector(""))