import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class GroqClient:
    def __init__(self, model: str = "openai/gpt-oss-120b"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a ReAct agent."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content