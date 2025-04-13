import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.tools import StructuredTool
from langchain import hub
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

print(f"model: {os.getenv("LLM_MODEL")} \n provider: {os.getenv("LLM_MODEL_PROVIDER")}")

# Initialize model dynamically from environment variables
llm = init_chat_model(model=os.getenv("LLM_MODEL"),
                      model_provider=os.getenv("LLM_MODEL_PROVIDER"))


# Define a structured tool for temperature conversion
def get_dhanam_value(a: float, b: float) -> float:
    """Finds the Dhanam value of two numbers."""
    try:
        return a + b - 32.0
    except Exception as e:
        print(f"Error: {e} | Input values: a={a}, b={b}")
        return None


# Define the structured tool
dhanam_tool = StructuredTool.from_function(
    func=get_dhanam_value,
    name="Dhanam Value Tool",
    description="Provides Dhanam value of two numbers.",
)


# Define tools list
tools = [dhanam_tool]

# Load the structured chat prompt
prompt = hub.pull("hwchase17/structured-chat-agent")

# Create the structured chat agent
agent = create_structured_chat_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Create the agent executor
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True,
                                                    handle_parsing_errors=True)

# Run the agent with structured input
response = agent_executor.invoke({"input": "Get Dhanam value of 19 and 17"})

print(f"\n🔹 Response: {response}")
