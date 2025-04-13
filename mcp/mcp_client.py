from mcp import ClientSession
from mcp.client.sse import sse_client
import asyncio


async def run():
    async with sse_client(url="http://127.0.0.1:8000/sse") as streams:
        async with ClientSession(*streams) as session:

            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"tools are {tools}")

            # Call a tool
            result = await session.call_tool("add", arguments={"a": 4, "b": 5})
            print(result.content[0].text)

            # Call a tool
            result = await session.call_tool("get_dhanam_value", arguments={"a": 4, "b": 5})
            print(result.content[0].text)

            # List available resources
            resources = await session.list_resources()
            print("resources", resources)

            # Read a resource
            content = await session.read_resource("resource://some_static_resource")
            print("content", content.contents[0].text)

            # Read a resource
            content = await session.read_resource("greeting://dhana")
            print("content", content.contents[0].text)

            # List available prompts
            prompts = await session.list_prompts()
            print("prompts", prompts)

            # Get a prompt
            prompt = await session.get_prompt(
                "review_code", arguments={"code": "print(\"Hello world\")"}
            )
            print("prompt", prompt)

            prompt = await session.get_prompt(
                "debug_error", arguments={"error": "SyntaxError: Null pointer error"}
            )
            print("prompt", prompt)


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        print(f"error is {e}")
