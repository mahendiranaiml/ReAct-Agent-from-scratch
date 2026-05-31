from app.agent.prompt_builder import build_react_prompt
from app.agent.parser import parse_action


class ReActAgent:
    def __init__(self, llm_client, tools: dict, max_steps: int = 5):
        self.llm = llm_client
        self.tools = tools
        self.max_steps = max_steps

    def run(self, query: str):

        prompt = build_react_prompt(query, self.tools)
        history = prompt

        for step in range(self.max_steps):

            # 1️⃣ Call LLM
            response = self.llm.generate(history)

            print("\n" + "=" * 60)
            print("LLM OUTPUT:")
            print(response)
            print("=" * 60)

            # 2️⃣ Parse output
            parsed = parse_action(response)

            print("PARSED:", parsed)

            # 3️⃣ If parsing fails → retry loop
            if not parsed:
                history += f"\n{response}\n"
                continue

            # 4️⃣ Final answer
            if parsed["type"] == "final":
                print("FINAL ANSWER:", parsed["answer"])
                return parsed["answer"]

            # 5️⃣ Tool execution
            tool_name = parsed["tool"]
            tool_input = parsed["input"]

            print("\nTOOL:", tool_name)
            print("INPUT:", tool_input)

            if tool_name not in self.tools:
                observation = f"Tool not found: {tool_name}"
            else:
                observation = self.tools[tool_name](tool_input)

            print("OBSERVATION:", observation)

            # 6️⃣ Feed back to LLM
            history += f"\n{response}\nObservation: {observation}\n"

        return "Max steps reached"