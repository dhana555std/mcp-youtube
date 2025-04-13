import asyncio
import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

from dotenv import load_dotenv

#Used to get the OPENAI_API_KEY from .env file.
load_dotenv()


async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Assistant",
        instructions="Use the tools to answer the questions.",
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="required"),
    )

    # Run the `get_random_fruit` tool
    message = "What's the random fruit? Provide one liner description about the fruit."
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def main():
    async with MCPServerSse(
        name="SSE Python Server",
        params={
            "url": "http://127.0.0.1:8000/sse",
        },
    ) as server:
        await run(server)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"{e}")