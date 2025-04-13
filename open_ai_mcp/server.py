import random

import requests
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("Server access by OpenAI.")

@mcp.tool()
def get_random_fruit() -> str:
    """Returns a random fruit."""
    print("[debug-server] get_random_fruit()")
    return random.choice(["Apple", "Banana", "Cherry", "Mango", "Batavia"])

if __name__ == "__main__":
    mcp.run(transport="sse")