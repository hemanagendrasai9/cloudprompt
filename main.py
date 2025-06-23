from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools.python.tool import PythonREPLTool

llm = OpenAI(temperature=0)

def simulate_aws_command(cmd: str):
    # Simulate cloud command execution
    return f"[SIMULATED]: Executed AWS Command: \{cmd\}"

tools = [
    Tool(name="SimulateAWS", func=simulate_aws_command, description="Executes AWS-related infra commands")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
