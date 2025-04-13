from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("MCP Server")


#### Tools ####
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b


@mcp.tool(name="get_dhanam_value", description="Get Dhanam value computed for a and b values.")
def get_dhanam_value(a: float, b: float) -> float:
    """Finds the Dhanam value of two numbers."""
    try:
        return a + b - 32.0
    except Exception as e:
        print(f"Error: {e} | Input values: a={a}, b={b}")
        return None

# More tools can be added here

#### Resources ####
# Add a static resource
@mcp.resource("resource://some_static_resource")
def get_static_resource() -> str:
    """Static resource data"""
    return "Any static data can be returned"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


#### Prompts ####
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    return [
        ("user", "I'm seeing this error:"),
        ("user", error),
        ("assistant", "I'll help debug that. What have you tried so far?"),
    ]


if __name__ == "__main__":
    # Initialize and run the server
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"error is {e}")

