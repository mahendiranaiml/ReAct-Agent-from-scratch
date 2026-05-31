from app.llm.client import GroqClient
from app.agent.react_loop import ReActAgent
from app.tools.registry import TOOLS


llm = GroqClient()

agent = ReActAgent(
    llm_client=llm,
    tools=TOOLS,
    max_steps=5
)

print(agent.run("What is 10 + 15 and 10 * 5"))