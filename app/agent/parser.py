import json

def parse_action(output: str):
    """
    Converts LLM JSON output into structured action
    """

    try:
        data = json.loads(output)

        action = data.get("action")

        if action == "final":
            return {
                "type": "final",
                "answer": data.get("answer", "")
            }

        return {
            "type": "tool",
            "tool": action,
            "input": data.get("input", "")
        }

    except Exception:
        # fallback if LLM breaks JSON
        return None